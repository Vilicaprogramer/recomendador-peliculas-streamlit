import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

df= pd.read_csv('df_sin_codificar_actores.csv')

def sentimental(opinion):
  model_name = "VerificadoProfesional/SaBERT-Spanish-Sentiment-Analysis"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSequenceClassification.from_pretrained(model_name)

  # Create the pipeline with truncation and padding
  pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, truncation=True, padding=True, device=0)
  
  return pipe(opinion)[0]['label']