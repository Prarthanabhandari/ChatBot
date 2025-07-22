from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import spacy
from spellchecker import SpellChecker
import language_tool_python
import os  # <-- imported os for environment variables

app = Flask(__name__)
CORS(app)

nlp = spacy.load("en_core_web_sm")
spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')  

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

    
    matches = tool.check(word)
    grammar_suggestions = []
    for match in matches:
        grammar_suggestions.append({
            "message": match.message,
            "replacements": match.replacements,
            "offset": match.offset,
            "errorLength": match.errorLength,
            "context": match.context,
            "sentence": match.sentence
        })

    return jsonify({
        "pos_info": pos_info,
        "affix_info": affix_info,
        "grammar": grammar_suggestions
    })

@app.route("/related", methods=["POST"])
def related_words():
    data = request.json
    word = data.get("word", "").strip().lower()

    prefix_related = set()
    suffix_related = set()

    
    for pre in prefixes:
        candidate = pre + word
        if is_meaningful(candidate):
            prefix_related.add(candidate)

    
    for suf in suffixes:
        candidate = word + suf
        if is_meaningful(candidate):
            suffix_related.add(candidate)

    return jsonify({
        "prefixes": sorted(prefix_related),
        "suffixes": sorted(suffix_related)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render or other hosting port
    app.run(host="0.0.0.0", port=port)
