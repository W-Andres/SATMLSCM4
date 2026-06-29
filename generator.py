import pandas as pd
import numpy as np
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataGenerator:
    def __init__(self, file_path="historico_cedis.csv", dias=30):
        """
        Inicializa la clase generadora de datos logísticos aceptando 'file_path' y 'dias'.
        """
        self.file_path = file_path
        self.dias = dias
        self.data = None

    def load_base_data(self):
        """
        Carga el archivo histórico base si existe en la ruta especificada.
        """
        if os.path.exists(self.file_path):
            try:
                self.data = pd.read_csv(self.file_path)
                logger.info(f"Archivo {self.file_path} cargado exitosamente.")
                return self.data
            except Exception as e:
                logger.error(f"Error al leer el archivo CSV: {str(e)}")
                raise e
        else:
            logger.warning(f"Archivo {self.file_path} no encontrado. Creando respaldo vacío.")
            self.data = pd.DataFrame(columns=["fecha", "cedis", "demanda", "sku", "tiempo_entrega"])
            return self.data

    def generar(self):
        """
        Método requerido explícitamente por la línea 241 de app.py.
        Retorna los datos cargados o genera un set de datos de respaldo.
        """
        self.load_base_data()
        
        # Si el archivo CSV base está vacío o no tiene registros, genera datos sintéticos simulados
        if self.data is None or self.data.empty:
            cedis_list = ['CEDIS_NORT', 'CEDIS_CENT', 'CEDIS_SUR']
            num_rows = int(self.dias) * 5  # Estimación basada en los días requeridos
            
            self.data = pd.DataFrame({
                "fecha": pd.date_range(end=pd.Timestamp.now(), periods=num_rows, freq="D").strftime('%Y-%m-%d'),
                "cedis": np.random.choice(cedis_list, size=num_rows),
                "demanda": np.random.randint(100, 1500, size=num_rows),
                "sku": [f"SKU-{np.random.randint(1000, 9999)}" for _ in range(num_rows)],
                "tiempo_entrega": np.random.randint(1, 7, size=num_rows)
            })
            logger.info("Datos sintéticos generados exitosamente ante la ausencia de registros base.")
            
        return self.data

    def generate_synthetic_data(self, num_rows=100):
        """Mantiene compatibilidad con llamadas secundarias externas."""
        return self.generar()

    def get_features_and_targets(self):
        """Mantiene compatibilidad con llamadas secundarias externas."""
        return self.generar()
