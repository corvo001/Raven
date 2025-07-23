from core.fractal_interpreter import FractalInterpreter
from core.pattern_classifier import PatternClassifier
from core.knowledge_base import KnowledgeBase
import numpy as np
import os

def main():
    print(" Iniciando Raven...")

    interpreter = FractalInterpreter()
    classifier = PatternClassifier(n_clusters=5)
    kb = KnowledgeBase()

    dataset_dir = "data/raw/"
    feature_vectors = []
    image_files = []

    for fname in os.listdir(dataset_dir):
        if fname.endswith(".png") or fname.endswith(".jpg"):
            path = os.path.join(dataset_dir, fname)
            features = interpreter.extract_features(path)
            vector = np.concatenate([
                features["hu_moments"],
                features["histogram"][:10]
            ])
            feature_vectors.append(vector)
            image_files.append(fname)

    if not feature_vectors:
        print("❌ No se encontraron imágenes válidas en /data/raw/")
        return

    print("✅ Extracción completada. Clasificando...")

    classifier.fit(feature_vectors)

    print("\n📊 Resultados:")
    for i, vec in enumerate(feature_vectors):
        cluster = classifier.predict(vec)
        desc = kb.describe_cluster(cluster)
        print(f"{image_files[i]} → Clase {cluster}: {desc}")

if __name__ == "__main__":
    main()
