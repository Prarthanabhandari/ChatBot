# 🧠 Linguistic Chatbot  
### Principles of Intelligent Language Processing & NLP-Based Interaction

![Python](https://img.shields.io/badge/Python-Backend-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-black)
![NLP](https://img.shields.io/badge/NLP-Processing-green)
![Status](https://img.shields.io/badge/Project-In%20Progress-orange)

---

## 🌍 Overview

The **Linguistic Chatbot** is an NLP-based system designed to **analyze, understand, and improve human language input**.

Unlike traditional chatbots, this system focuses on:
- Linguistic correctness  
- Structural clarity  
- Meaningful interpretation  

It acts as a **language analysis engine** that applies Natural Language Processing (NLP) techniques.

---

## 📌 Philosophy

> **“A good system does not just respond — it understands.”**

👉 Every input must be **analyzed, not just answered**

---

## 🎯 Core Objectives

- 🏷 Perform Part-of-Speech (POS) tagging  
- 🧩 Morphological analysis (prefix, suffix, infix)  
- 🌱 Extract meaningful root words  
- 🔍 Detect and correct spelling mistakes  
- ✍ Improve grammar and sentence structure  
- 🧠 Maintain context awareness  
- 🎤 Enable speech interaction  

---

## ⚙️ System Architecture

The chatbot uses a **modular architecture**:

- Input Processor  
- Tokenizer  
- Spell Checker  
- Morphological Analyzer  
- POS Tagger  
- Root Word Analyzer  
- Grammar Correction Engine  
- Response Generator  
- Speech Module  

---

## 🔄 Processing Pipeline

User Input
↓
Tokenization
↓
Spell Checking & Suggestions
↓
Morphological Analysis
↓
POS Tagging
↓
Root Word Extraction
↓
Grammar Correction
↓
Response Generation
↓
Output (Text / Speech)



---

## ✨ Features

### 🏷️ Part-of-Speech Tagging
Classifies words into:
- Noun  
- Verb  
- Adjective  
- Adverb  
- Pronoun  

---

### 🧩 Morphological Analysis

- Prefix → *unhappy = un + happy*  
- Suffix → *running = run + ing*  
- Infix/Internal → *stands = stand + s*  

✔ Improves accuracy  
✔ Prevents incorrect splitting  

---

### 🌱 Root Word Extraction

❌ Incorrect: `runn`  
✅ Correct: `run`  

---

### 🔍 Spell Checking

- Dictionary validation  
- Tools used:
  - pyenchant  
  - pyspellchecker  

---

### ✍️ Grammar Correction

- Improves sentence structure  
- Suggests natural phrasing  

---

### 🧠 Context Awareness

- Understands word relationships  
- Avoids isolated corrections  

---

### 🎤 Speech Integration

- Speech-to-Text (Input)  
- Text-to-Speech (Output)  

---

### 📝 Word History Tracking

- Maintains session history  
- Improves interaction continuity  

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|----------|
| Backend | Python (Flask) |
| NLP Libraries | NLTK, pyenchant, pyspellchecker |
| Frontend | HTML5, CSS3, JavaScript |
| APIs | Web Speech API |

---

## 📂 Project Working

-He is unhappy and runing fastly

Output
-✅ Corrected Sentence:
-He is unhappy and running fast
-🧩 Morphological Analysis:
-unhappy → un + happy
-running → run + ing
-🏷 POS Tags:
-Pronoun | Verb | Adjective | Conjunction | Verb | Adverb
-🌱 Root Words:
-happy, run, fast

## 📂 Project Structure


linguistic-chatbot/
│── static/
│ ├── css/
│ └── js/
│── templates/
│ └── index.html
│── app.py
│── requirements.txt
│── README.md


---

## ⚙️ Installation & Setup



```bash
cd linguistic-chatbot

pip install -r requirements.txt

python app.py

git clone https://github.com/your-username/linguistic-chatbot.git



