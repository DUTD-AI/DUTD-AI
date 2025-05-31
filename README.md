# 🚑 DUTD.AI – Detector of Urinary Tract Diseases using AI

**DUTD.AI** is a Flask-based web application that uses machine learning to predict urinary tract diseases (UTDs) based on user health input. Built for accessibility, the system enables fast, early diagnosis directly from a simple web interface.

🌐 **Live App**: [https://dutd-ai.onrender.com](https://dutd-ai.onrender.com)

---

## ⚙️ Key Features

- 🧠 AI-powered prediction using Support Vector Machine (SVM)
- 📋 Simple form-based health data input
- 📊 Instant result display with diagnosis
- 🎨 Clean interface with styled templates
- 🔁 Scalable and deployable (tested on [Render](https://render.com))

---

## 🚀 Getting Started

### Clone & Run Locally

```bash
git clone https://github.com/DUTD-AI/DUTD-AI.git
cd DUTD-AI
pip install -r requirements.txt
python app.py
```

Then open your browser at: `http://127.0.0.1:5000/`

---

## 🗂 Project Structure

```
DUTD-AI/
│   app.py                  # Main Flask application
│   Procfile                # Deployment config (Render)
│   requirements.txt        # Dependencies
│   scaler.pkl              # Pre-trained scaler
│   svm_model.pkl           # Trained SVM classifier
│
├───static/
│   ├── Icon.png
│   ├── index_back.png
│   ├── predict_back.png
│   ├── result_back.png
│   └── style.css
│
└───templates/
    ├── index.html          # Homepage
    ├── predict.html        # Data input form
    └── result.html         # Result/diagnosis output
```

