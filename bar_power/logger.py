import logging, os
from bar_power.config import Config

configutation = Config()
LOG_DIRECTORY = configutation.get_log_directory()
LOG_FILE      = configutation.get_log_file()

if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY, exist_ok=True)

logging.basicConfig(filename=LOG_DIRECTORY + LOG_FILE, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s' )
