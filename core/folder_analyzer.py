import os
from datetime import datetime

class FolderAnalyzer:
    @staticmethod
    def get_todays_folder(base_path):
        """Identifica la carpeta con la fecha de hoy en formato DDMMYYYY"""
        today = datetime.now().strftime("%d%m%Y")  # Formato: 24072025
        print(f"Buscando carpeta para la fecha: {today}")
        
        today_path = os.path.join(base_path, 'today')  # Ruta a la carpeta 'today'
        
        # Imprimir todas las carpetas en 'today'
        print("Carpetas en 'today':")
        for folder in os.listdir(today_path):
            print(f"Carpeta encontrada: {folder}")
        
        if today in os.listdir(today_path):
            return os.path.join(today_path, today)
        
        print("🔍 No se encontró la carpeta de hoy.")
        return None
