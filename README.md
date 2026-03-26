# 🚨 Toxic Comment Classification Web App

An end-to-end machine learning project that detects and classifies toxic comments using NLP models and deploys them as an interactive web application.

---

## 📌 Project Overview

Online platforms face challenges with toxic and abusive language. This project builds a **text classification system** that automatically detects toxic comments in real time.

The system is designed as a **production-ready pipeline**:
- Model trained for toxicity detection  
- Hosted on Hugging Face  
- Deployed as an interactive web app using Streamlit  

---

## 🎯 Key Features

- ✅ Real-time toxic comment detection  
- ✅ User input text classification  
- ✅ Confidence score output  
- ✅ Interactive web interface  
- ✅ Model loaded from Hugging Face Hub  

---

## 🧠 Model Details

- Model Type: Transformer-based NLP model  
- Framework: Hugging Face Transformers  
- Task: Toxic vs Non-toxic classification  
- Backend: PyTorch  

---

## ⚙️ Tech Stack

- Python  
- Streamlit  
- Hugging Face Transformers  
- PyTorch  
- Scikit-learn  
- GitHub  

---

## 🏗️ Project Structure

```bash
toxic-comment-streamlit/
│
├── app.py
├── requirements.txt
├── README.md
```

---

## 🚀 How It Works

1. User enters text in the web app  
2. Text is tokenized using a pretrained tokenizer  
3. Model predicts toxicity score  
4. Result is displayed with confidence  

---

## 💻 Run Locally

### Clone the repository
```bash
git clone https://github.com/CharanKonduru2024/toxic-comment-streamlit.git
cd toxic-comment-streamlit
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the app
```bash
streamlit run app.py
```

---

## 🌐 Model Loading

The model is loaded directly from Hugging Face:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "Charan789/deberta-toxic"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
```

---

## 📊 Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-score  

---

## 🧪 Example

**Input:**
```
You are stupid and useless
```

**Output:**
```
Toxic Comment (Confidence: 0.94)
```

---

## 🔥 Deployment

- Code hosted on GitHub  
- Model hosted on Hugging Face  
- App deployed using Streamlit Cloud  

