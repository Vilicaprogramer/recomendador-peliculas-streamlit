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
- **Scikit-learn**: Implementación de KMeans para clustering.
- **Funciones personalizadas**: Manejo de recomendaciones y análisis de sentimientos.

---

## 📁 Estructura del Proyecto
📂 recomendador-peliculas-streamlit
├── 📂 __pycache__                # Archivos caché generados por Python
├── 📄 .streamlit                # Configuración personalizada para Streamlit
├── 📄 .gitattributes            # Configuraciones específicas para Git
├── 📄 .gitignore                # Archivos y carpetas a ignorar por Git
├── 📄 codificacion_generos.json # Archivo JSON con información de géneros codificados
├── 📄 df_recomendador.csv       # Dataset inicial para recomendaciones tras aplicarle un KMeans
├── 📄 df_recomendador2.csv      # Segunda versión del dataset en el que se hizo un primer HDBSCAN con menos volumen de películas.
├── 📄 df_recomendador3.csv      # Dataset principal utilizado en la aplicación
├── 📄 df_sin_codificar_actores.csv # Dataset base con el que se ha realizado todo el procesamiento
├── 📄 functions_recomend.py     # Funciones personalizadas para recomendaciones
├── 📄 recomendador.ipynb        # Notebook para análisis y pruebas de desarrollo
├── 📄 recomendador.py           # Script principal que carga la página e interactúa con las funciones
├── 📄 sentimental.py            # Función para análisis de sentimientos
└── 📄 README.md                 # Documentación del proyecto


## 📊 Dataset
El dataset utilizado, **df_recomendador3.csv**, contiene información detallada de películas, incluyendo:

- Título 🎥
- Año 📆
- Director 🎬
- Actores principales 👥
- Géneros 🎭
- Sinopsis 📝