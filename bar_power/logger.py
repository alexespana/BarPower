import logging, os
from bar_power.config import Config

configuration = Config()
LOG_DIRECTORY = configuration.get_log_directory()
LOG_FILE      = configuration.get_log_file()

if not os.path.exists(LOG_DIRECTORY):
    try:
        os.makedirs(LOG_DIRECTORY, exist_ok=True)
    except OSError:
        raise OSError("Error al intentar crear el directorio ")

logging.basicConfig(filename=LOG_DIRECTORY + LOG_FILE, level=logging.DEBUG, format='%(asctime)s <=> %(levelname)s <=> %(pathname)s <=> %(message)s' )
