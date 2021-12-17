import etcd3, os
from dotenv import load_dotenv

class Config:
    """
    Clase que representa la configuración de la aplicación
    """
    def __init__(self):
        try:
            etcd_client = etcd3.client()
            self.log_directory = etcd_client.get(LOG_DIR_VAR_NAME)[0].decode("utf8")
            self.log_file = etcd_client.get(LOG_FILE_VAR_NAME)[0].decode("utf8")
        except:
            load_dotenv('config.env')
            if (os.getenv('LOG_DIR')):
                self.log_directory = os.getenv('LOG_DIR')
            else:
                self.log_directory = '/tmp/barpower/log/'   # Lugar con permisos de escritura

            if(os.getenv('LOG_FILE')):
                self.log_file = os.getenv('LOG_FILE')
            else:
                self.log_file = 'bar_power.log'

    
    def get_log_directory(self):
        """
        Obtiene la ruta del directorio donde se almacenan los logs

        Returns
        --------
        log_directory: str
            Ruta del directorio donde se almacenan los logs
        """
        return self.log_directory

    def get_log_file(self):
        """
        Obtiene el nombre del fichero donde se almacenan los logs

        Returns
        --------
        log_file: str
            Archivo donde se almacenan los logs
        """
        return self.log_file
