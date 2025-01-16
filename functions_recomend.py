import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

df= pd.read_csv('df_sin_codificar_actores.csv')

# Definimos una función para realizar análisis de sentimiento utilizando un modelo pre-entrenado
def sentimental(opinion):
  # Consideramos el modelo SaBERT para análisis de sentimiento en español
  model_name = "VerificadoProfesional/SaBERT-Spanish-Sentiment-Analysis"
  # Cargamos el tokenizador y el modelo pre-entrenado
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSequenceClassification.from_pretrained(model_name)

  # Creamos un pipeline para análisis de sentimiento, habilitando el truncamiento y padding para manejar secuencias de diferentes longitudes
  pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, truncation=True, padding=True, device=0)
  
  # Aplicamos el pipeline a la opinión de entrada y retornamos la etiqueta del sentimiento
  return pipe(opinion)[0]['label']


# Definimos una función recomendadora que proporciona películas similares basadas en el cluster
def recomendador(pelicula, df=df):
  # Consideramos el cluster asociado a la película de entrada
  cluster = df['cluster'][df['titulo'] == pelicula]
  # Creamos un DataFrame que contiene sólo las peliculas que pertenecen al mismo cluster que la pelicula de entrada
  df_cluster = df[df['cluster'] == cluster.iloc[0]]
  # Filtramos el DataFrame para excluir la película de entrada
  df_cluster = df_cluster[df_cluster['titulo'] != pelicula]

  # Retornamos una muestra aleatoria de 5 películas del mismo clúster
  return df_cluster.sample(5)