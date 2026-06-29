import logging
import os

class LoggerManager:
    """
    Administrador centralizado de registros para el sistema SAT-ML SCM.
    """
    @staticmethod
    def get_logger(name=__name__):
        logger = logging.getLogger(name)
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
            # Consola
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
            
        return logger

