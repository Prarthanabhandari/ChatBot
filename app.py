from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import spacy
from spellchecker import SpellChecker

app = Flask(__name__)
CORS(app)

nlp = spacy.load("en_core_web_sm")
spell = SpellChecker()

prefixes = [
    "un", "re", "pre", "in", "dis", "mis", "im", "ir", "il", "non", "post", "inter",
    "sub", "super", "under", "over", "anti", "auto", "bi", "tri", "mono", "multi",
    "trans", "co", "ex", "pro", "en", "semi", "de"
]

suffixes = [
    "ward", "ive", "en", "y", "ible", "less", "ful", "ous", "al", "ity", "ship", "ence", "ance",
    "sion", "tion", "ment", "ness", "ian", "ist", "or", "er", "able", "ing", "ed", "ly"
]

def is_meaningful(word):
    return len(word) > 2 and word in spell

def analyze_affixes(word):
    affix_info = []
    prefix_found = None
    suffix_found = None
    root = word

    # Try prefix removal first
    for pre in sorted(prefixes, key=len, reverse=True):
        if word.startswith(pre):
            possible_root = word[len(pre):]
            if is_meaningful(possible_root):
                prefix_found = pre
                root = possible_root
                affix_info.append({
                    "type": "prefix",
                    "affix": prefix_found,
                    "root_word": root
                })
                break

    # Then try suffix on the current root
    for suf in sorted(suffixes, key=len, reverse=True):
        if root.endswith(suf):
            possible_root = root[:-len(suf)]
            if is_meaningful(possible_root):
                suffix_found = suf
                root = possible_root
                affix_info.append({
                    "type": "suffix",
                    "affix": suffix_found,
                    "root_word": root
                })
                break

    if not affix_info:
        affix_info.append({"type": "none", "message": "No meaningful prefix/suffix found"})

    return affix_info

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    word = data.get("word", "").strip().lower()

    if not word.isalpha():
        return jsonify({"error": "Invalid word."}), 400

    doc = nlp(word)
    pos_info = [{"word": token.text, "pos": token.pos_, "tag": token.tag_} for token in doc]
    affix_info = analyze_affixes(word)

    return jsonify({
        "pos_info": pos_info,
        "affix_info": affix_info
    })

if __name__ == "__main__":
    app.run(debug=True)
