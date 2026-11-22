# Configuración del archivo de logs
# Aquí se registran eventos y errores del sistema.

import logging
from pathlib import Path


def configurar_logger():
    """Crea y configura el logger para guardar eventos en logs/sistema.log."""
    carpeta_logs = Path(__file__).resolve().parent / "logs"
    carpeta_logs.mkdir(exist_ok=True)
    archivo_log = carpeta_logs / "sistema.log"

    logger = logging.getLogger("software_fj")
    logger.setLevel(logging.INFO)

    # Evitar duplicar handlers si se configura más de una vez
    if not logger.handlers:
        handler = logging.FileHandler(archivo_log, encoding="utf-8")
        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formato)
        logger.addHandler(handler)

    return logger
