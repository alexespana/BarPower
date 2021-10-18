class Visits:
    """
    Entidad para almacenar la información sobre las visitas al bar de distintos tipos de 
    clientes y las comandas que se hacen en unas franjas horarias.

    Attributes
    ----------
    data : dict
        Datos las visitas al bar de distintos tipos de clientes y las comandas 
        que se hacen en unas franjas horarias.
    """

    def __init__(self):
        """
        Constructor de la entidad
        """

        self.data = {}

