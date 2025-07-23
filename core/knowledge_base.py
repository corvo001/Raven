class KnowledgeBase:
    def describe_cluster(self, cluster_id):
        descriptions = {
            0: "Formas circulares concéntricas, tipo Mandelbrot.",
            1: "Filamentos tipo helecho, ramificación suave.",
            2: "Simetría axial, patrones tipo Julia.",
            3: "Caos denso sin bordes definidos.",
            4: "Estructuras arborescentes, raíces o venas."
        }
        return descriptions.get(cluster_id, "Sin descripción asignada.")
