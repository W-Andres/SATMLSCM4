import pandas as pd
import numpy as np
import os
import logging

# Configuración de un logger local e independiente
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataGenerator:
    def __init__(self, file_path="historico_cedis.csv"):
        """
        Inicializa la clase generadora de datos logísticos.
        """
        self.file_path = file_path
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
            # Si el archivo no se encuentra, genera un DataFrame vacío estructurado de respaldo
            logger.warning(f"Archivo {self.file_path} no encontrado. Creando respaldo vacío.")
            self.data = pd.DataFrame(columns=["fecha", "cedis", "demanda", "sku", "tiempo_entrega"])
            return self.data

    def generate_synthetic_data(self, num_rows=100):
        """
        Genera filas de datos sintéticos basados en la distribución u operaciones 
        necesarias para los modelos predictivos del SAT-ML SCM.
        """
        if self.data is None or self.data.empty:
            self.load_base_data()

        cedis_list = ['CEDIS_NORT', 'CEDIS_CENT', 'CEDIS_SUR']
        
        synthetic_df = pd.DataFrame({
            "fecha": pd.date_range(start="2026-01-01", periods=num_rows, freq="D").strftime('%Y-%m-%d'),
            "cedis": np.random.choice(cedis_list, size=num_rows),
            "demanda": np.random.randint(100, 1500, size=num_rows),
            "sku": [f"SKU-{np.random.randint(1000, 9999)}" for _ in range(num_rows)],
            "tiempo_entrega": np.random.randint(1, 7, size=num_rows)
        })
        
        return synthetic_df

    def get_features_and_targets(self):
        """
        Prepara los conjuntos de datos limpios para enviarlos a evaluate.py o app.py
        """
        if self.data is None:
            self.load_base_data()
        
        return self.data
