# recomendador-peliculas-streamlit
 # 🎬 Recomendador de Películas con Streamlit

¡Bienvenido al **Recomendador de Películas**! 🍿 Esta aplicación, desarrollada con **Streamlit**, utiliza **machine learning** y clustering para ofrecer recomendaciones personalizadas basadas en tus películas favoritas. Solo selecciona una película y obtendrás una lista de recomendaciones que seguramente te encantarán. 🌟

---

## 🚀 Funcionalidades

- 🔍 **Selector de Películas**: Escoge una película de la lista desplegable.
- ⭐ **Calificación con Estrellas**: Valora las películas que has visto.
- 💬 **Opiniones de Usuarios**: Comparte tu opinión sobre las películas.
- 🤖 **Recomendaciones Inteligentes**: Basadas en el análisis de clustering (HDBSCAN).
- 📜 **Detalles de las Películas**: Títulos, géneros, elenco y una breve sinopsis.
- 🎨 **Interfaz Interactiva y Fácil de Usar**: Diseñada con Streamlit para una experiencia fluida.

---

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje principal de desarrollo.
- **Streamlit**: Para crear la interfaz web interactiva.
- **Pandas**: Manipulación de datos.
- **NumPy**: Cálculos matemáticos eficientes.
- **Scikit-learn**: Implementación de DBSCAN para clustering.
- **Funciones personalizadas**: Manejo de recomendaciones y análisis de sentimientos.

---

## 📁 Estructura del Proyecto

```plaintext
recomendador-peliculas-streamlit/
├── __pycache__/                # Archivos caché generados por Python
├── .streamlit/                 # Configuración personalizada para Streamlit
├── .gitattributes              # Configuraciones específicas para Git
├── .gitignore                  # Archivos y carpetas a ignorar por Git
├── codificacion_generos.json   # Archivo JSON con información de géneros codificados
├── df_recomendador.csv         # Dataset inicial para recomendaciones tras aplicarle un KMeans
├── df_recomendador2.csv        # Segunda versión del dataset (primer HDBSCAN con menos datos)
├── df_recomendador3.csv        # Dataset principal utilizado en la aplicación
├── df_sin_codificar_actores.csv # Dataset base usado para procesamiento
├── functions_recomend.py       # Funciones personalizadas para recomendaciones
├── recomendador.ipynb          # Notebook para análisis y pruebas de desarrollo
├── recomendador.py             # Script principal que carga la página e interactúa con las funciones
├── sentimental.py              # Función para análisis de sentimientos
└── README.md                   # Documentación del proyecto
```
---

## 📊 Dataset
El dataset utilizado, **df_recomendador3.csv**, contiene información detallada de películas, incluyendo:

- Título 🎥
- Año 📆
- Director 🎬
- Actores principales 👥
- Géneros 🎭
- Sinopsis 📝

---

## 🖥️ ¿Cómo Usar el Recomendador?

Sigue estos pasos para disfrutar de recomendaciones personalizadas de películas:

1. **Ejecuta la Aplicación**  
   - Clona el repositorio de forma local
   - Asegúrate de tener instaladas las dependencias necesarias. 
   - Desde la terminal, ejecuta el siguiente comando:  
     ```bash
     streamlit run recomendador.py
     ```
   - Esto abrirá la aplicación en tu navegador.

2. **Selecciona una Película**  
   - En el menú lateral de la aplicación, encontrarás un selector desplegable con una lista de películas disponibles.  
   - Escoge la película que hayas visto o que te guste para recibir recomendaciones similares.

3. **Da tu Opinión**  
   - Valora la película seleccionada usando las estrellas que encontrarás en el menú lateral.  
   - Escribe una opinión breve en el campo de texto proporcionado.  
   - Haz clic en el botón "Enviar" para que tu feedback se procese.

4. **Descubre Nuevas Películas**  
   - La aplicación generará una lista de 5 películas recomendadas, basadas en tus selecciones y análisis de clustering.  
   - Para cada recomendación, verás:
     - **Título**  
     - **Año de estreno**  
     - **Director**  
     - **Elenco principal**  
     - **Géneros**  
     - **Sinopsis**  

5. **Explora y Disfruta**  
   - Revisa las recomendaciones y elige tu próxima película para disfrutar. 🎬 

Así de simple, ¡encuentra tu próxima película favorita! 🍿

---
