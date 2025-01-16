import streamlit as st
import pandas as pd
import numpy as np
import time
import functions_recomend as fr

from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

# Cargamos el DataFrame que contiene información de las películas desde un archivo CSV
df = pd.read_csv('df_recomendador3.csv')

# Creamos el título principal de la aplicación en Streamlit
st.title('***Recomendador de :blue[peliculas]*** 🎬')
# Añadimos un subtítulo para dar la bienvenida al usuario
st.subheader('_Bienvenido a la aplicación de recomendación de películas._')

# Explicamos el funcionamiento de la aplicación
st.write('En esta aplicación, podrás encontrar películas similares a las que has visto. Para ello, \
         selecciona una película de la lista y te recomendaremos 5 películas similares. ¡Disfruta de la experiencia!')

# Creamos un selector desplegable en la barra lateral para que el usuario seleccione una película
option = st.sidebar.selectbox(
    '¿Que película has visto?', 
    df['titulo'].sort_values(ascending=True),
    index=None,
    placeholder="Selecciona una película... ")

# Añadimos una pregunta de feedback en la barra lateral usando estrellas
st.sidebar.write('¿Cuanto te ha gustado?')
st.sidebar.feedback('stars')

# Creamos un campo de texto en la barra lateral para que el usuario ingrese su opinión sobre la película
text = st.sidebar.text_input('¿Que opinas de la pelicula?', '', placeholder= 'Introduce aqui tu opinion...')
# Creamos un botón para enviar la opinión del usuario
button = st.sidebar.button('Enviar')

# Si el usuario hace clic en el botón 'Enviar', se ejecuta el siguiente bloque de código
if button:
    # Utilizamos la función de análisis de sentimiento para determinar si la opinión es positiva o negativa
    st.sidebar.write(f'Muy bien veo que la película "{option}": ', '**Te gustó**' if fr.sentimental(text) == 'Positive' else '**No te gustó**')
    # Obtenemos una lista de 5 películas recomendadas usando la función recomendador
    recomendador = fr.recomendador(option, df)
    # Iteramos sobre las películas recomendadas para mostrarlas en la interfaz
    for i in range(5):
        # Creamos un contenedor para cada recomendación
        with st.container(height=380):
            # Mostramos un encabezado para cada película recomendada
            st.markdown(f':blue-background[**Película {i+1}**]')
            # Mostramos el título, año y director de la película, usando HTML para el espaciado
            st.markdown(f"***Titulo:*** {recomendador.iloc[i]['titulo']}{' '*12}***Año:*** {'Sin año de estreno' if pd.isna(recomendador.iloc[i]['ano']) else int(recomendador.iloc[i]['ano'])}{' '*12}***Director:*** {recomendador.iloc[i]['director']}", unsafe_allow_html=True)
            # Mostramos los actores principales de la película
            st.markdown(f"***Actores:*** {recomendador.iloc[i]['actor_1']},{' '*4}{recomendador.iloc[i]['actor_2']},{' '*4}{recomendador.iloc[i]['actor_3']}{' '*12}***Duración:*** {int(recomendador.iloc[i]['duracion'])} min", unsafe_allow_html=True)
            # Obtenemos los géneros de la película y los mostramos con espaciado
            generos = set([recomendador.iloc[i]['genero_1'], recomendador.iloc[i]['genero_2'], recomendador.iloc[i]['genero_3']])
            espacios = " " * 4
            generos_con_espacios = f",{espacios}".join(generos)
            st.markdown(f"***Géneros:*** {generos_con_espacios}", unsafe_allow_html=True)
            # Mostramos la sinopsis de la película en un área de texto
            st.text_area("***Sinopsis***", 'Sinopsis no disponible' if pd.isna(recomendador.iloc[i]['sinopsis']) else recomendador.iloc[i]['sinopsis'] , height=150)
