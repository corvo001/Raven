import json
import os
import re
import shutil
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from core.fractal_interpreter import FractalInterpreter
from core.pattern_classifier import PatternClassifier
from core.knowledge_base import KnowledgeBase
from core.folder_analyzer import FolderAnalyzer

def natural_sort_key(s):
    """Función para ordenar numéricamente los nombres de archivo."""
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split('([0-9]+)', s)]

def save_classification(image_path, cluster, description):
    """Guarda o sobrescribe la clasificación en un archivo JSON"""
    json_path = os.path.splitext(image_path)[0] + '.json'
    classification_data = {
        'image_filename': os.path.basename(image_path),
        'cluster': int(cluster),
        'cluster_description': description,
        'last_processed': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'version': '1.0'
    }
    
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(classification_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Error guardando JSON para {image_path}: {e}")

def main():
    print("🔄 Iniciando Raven...")

    interpreter = FractalInterpreter()
    classifier = PatternClassifier(n_clusters=5)
    kb = KnowledgeBase()
    scaler = StandardScaler()

    base_data_path = "data/"
    today_folder = FolderAnalyzer.get_todays_folder(base_data_path)

    if not today_folder:
        print("❌ No se encontró una carpeta para la fecha de hoy.")
        return

    print(f"📁 Carpeta de hoy encontrada: {today_folder}")

    # Obtener y ordenar archivos numéricamente en la carpeta de hoy
    image_files = sorted(
        [f for f in os.listdir(today_folder) if f.endswith((".png", ".jpg"))],
        key=natural_sort_key
    )
    
    # Procesar imágenes y extraer características
    feature_vectors = []
    processed_files = []

    for fname in image_files:
        path = os.path.join(today_folder, fname)
        try:
            features = interpreter.extract_features(path)
            vector = np.concatenate([
                features["hu_moments"],
                features["histogram"][:10]
            ])
            feature_vectors.append(vector)
            processed_files.append(fname)
        except Exception as e:
            print(f"⚠️ Error procesando {fname}: {e}")

    if not feature_vectors:
        print("❌ No se encontraron imágenes válidas")
        return

    # Escalado y clustering
    feature_vectors_np = np.array(feature_vectors)
    scaled_vectors = scaler.fit_transform(feature_vectors_np)
    classifier.fit(scaled_vectors)

    # Mostrar y guardar resultados
    print("\n📊 Resultados ordenados:")
    for vec, fname in zip(feature_vectors_np, processed_files):
        img_path = os.path.join(today_folder, fname)
        scaled_vec = scaler.transform([vec])[0]
        cluster = classifier.predict(scaled_vec)
        desc = kb.describe_cluster(cluster)
        
        print(f"{fname} → Clase {cluster}: {desc}")
        save_classification(img_path, cluster, desc)

    # Mover carpeta procesada a 'processed'
    processed_dir = os.path.join(base_data_path, "processed")
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    folder_name = os.path.basename(today_folder)
    destination = os.path.join(processed_dir, folder_name)
    
    try:
        shutil.move(today_folder, destination)
        print(f"\n✅ Carpeta movida a procesados: {destination}")
    except Exception as e:
        print(f"⚠️ Error moviendo carpeta: {e}")

if __name__ == "__main__":
    main()
