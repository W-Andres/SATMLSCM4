import logging

class LoggerManager:
    """
    Administrador central de registros (Logs) para SAT-ML SCM.
    """
    @staticmethod
    def get_logger(name="SAT-ML-SCM"):
        logger = logging.getLogger(name)
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
            # Handler para la consola de Streamlit Cloud
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
            
        return logger


