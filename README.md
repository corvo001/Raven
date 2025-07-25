# Raven 0.2

**Raven** es una inteligencia artificial escalable desarrollada en Python, diseñada para interpretar patrones fractales complejos y clasificarlos con base en sus propiedades visuales. Su objetivo no es generar nuevos fractales, sino **analizarlos, detectar patrones, categorizarlos** y vincularlos con conocimiento humano relevante, usando técnicas de visión computacional y machine learning.

##  Objetivo

- **Analizar imágenes fractales** mediante extracción de características (contornos, histogramas, momentos de Hu)
- **Clasificarlas en grupos visuales** similares mediante clustering (KMeans)
- **Asociar cada grupo** a descripciones interpretativas humanas
- **Aprender progresivamente** a diferenciar estilos y estructuras fractales

##  Novedades en la versión actual

- **Mejoras en el algoritmo de clasificación**: Mayor precisión en la detección de patrones
- **Optimización de rendimiento**: Procesamiento más rápido de imágenes fractales
- **Nueva interfaz de visualización**: Mejor representación de los clusters encontrados
- **Base de conocimiento expandida**: Más categorías y descripciones interpretativas
- **Soporte para formatos adicionales**: Compatible con más tipos de archivos de imagen

##  Instalación

```bash
# Clona el repositorio
git clone https://github.com/tuusuario/raven.git
cd raven

# Instala las dependencias
pip install numpy opencv-python scikit-learn matplotlib

# O usando requirements.txt (si está disponible)
pip install -r requirements.txt
```

## 📁 Estructura del proyecto

```
raven_ai/
├── main.py                      # Punto de entrada principal
├── core/
│   ├── fractal_interpreter.py   # Análisis e interpretación de fractales
│   ├── pattern_classifier.py    # Clasificación y clustering
│   ├── knowledge_base.py        # Base de conocimiento interpretativo
│   └── utils.py                 # Utilidades auxiliares
├── data/
│   ├── raw/                     # Imágenes fractales de entrada
│   └── features/                # Descriptores extraídos
├── models/                      # Clasificadores entrenados
├── notebooks/                   # Análisis exploratorios y ejemplos
├── tests/                       # Pruebas unitarias
└── README.md
```

## 📖 Uso básico

```python
from core.fractal_interpreter import FractalInterpreter
from core.pattern_classifier import PatternClassifier

# Inicializar Raven
interpreter = FractalInterpreter()
classifier = PatternClassifier()

# Analizar una imagen fractal
features = interpreter.analyze_fractal("data/raw/mi_fractal.png")

# Clasificar el patrón
cluster = classifier.classify_pattern(features)

# Obtener interpretación
interpretation = classifier.get_interpretation(cluster)
print(f"Interpretación: {interpretation}")
```

## 🔧 Configuración avanzada

```python
# Configurar parámetros del clasificador
classifier_config = {
    "n_clusters": 10,
    "feature_weights": {
        "contours": 0.4,
        "histogram": 0.3,
        "hu_moments": 0.3
    }
}

classifier = PatternClassifier(config=classifier_config)
```

##  Requisitos del sistema

- **Python**: >= 3.8
- **NumPy**: >= 1.19.0
- **OpenCV**: >= 4.5.0
- **Scikit-learn**: >= 1.0.0
- **Matplotlib**: >= 3.3.0

##  Ejecutar pruebas

```bash
# Ejecutar todas las pruebas
python -m pytest tests/

# Ejecutar pruebas específicas
python -m pytest tests/test_fractal_interpreter.py
```

##  Ejemplos de uso

Consulta la carpeta `notebooks/` para ejemplos detallados:

- `01_analisis_basico.ipynb`: Análisis básico de fractales
- `02_clustering_avanzado.ipynb`: Técnicas avanzadas de clustering
- `03_interpretacion_patrones.ipynb`: Interpretación y visualización de patrones

##  Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. **Fork** el proyecto
2. Crea una **rama** para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. **Commit** tus cambios (`git commit -m 'Añadir nueva característica'`)
4. **Push** a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un **Pull Request**

### Guías de contribución

- Sigue las convenciones de código PEP 8
- Añade pruebas para nuevas funcionalidades
- Documenta el código usando docstrings
- Actualiza el README si es necesario

## Reportar problemas

Si encuentras un bug o tienes una sugerencia, por favor:

1. Revisa si ya existe un issue similar
2. Crea un nuevo issue con una descripción detallada
3. Incluye ejemplos de código si es posible
4. Especifica tu entorno (OS, versión de Python, etc.)

##  Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

##  Agradecimientos

- A la comunidad científica que estudia fractales
- A los desarrolladores de OpenCV y Scikit-learn
- A todos los contribuidores del proyecto

##  Referencias

- [Documentación completa](docs/)
- [API Reference](docs/api.md)
- [Tutoriales](notebooks/)
- [Changelog](CHANGELOG.md)

---

**Desarrollado por Corvo para el análisis inteligente de patrones fractales**

