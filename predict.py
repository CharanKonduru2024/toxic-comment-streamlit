from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

model_dir = "model"
tokenizer = AutoTokenizer.from_pretrained("Charan789/deberta-toxic")
model = AutoModelForSequenceClassification.from_pretrained("Charan789/deberta-toxic")
model.eval()

LABELS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

def predict_toxicity(comment):
    inputs = tokenizer(comment, return_tensors="pt", truncation=True, padding=True, max_length=256)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.sigmoid(outputs.logits).squeeze().numpy()
    
    return {label: f"{round(prob * 100, 2)}%" if prob > 0.5 else "No" for label, prob in zip(LABELS, probs)}
