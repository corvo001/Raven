import cv2
import numpy as np

class FractalInterpreter:
    def extract_features(self, image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(f"Imagen no encontrada: {image_path}")

        # Contornos y bordes
        edges = cv2.Canny(img, 100, 200)

        # Histograma de niveles de gris
        hist = cv2.calcHist([img], [0], None, [256], [0, 256]).flatten()

        # Momentos de Hu (forma)
        moments = cv2.moments(edges)
        hu = cv2.HuMoments(moments).flatten()

        return {
            "edges": edges,
            "histogram": hist,
            "hu_moments": hu
        }
