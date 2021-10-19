from datetime import *

class Visits:
    """
    Entidad para almacenar la información sobre las visitas al bar de distintos tipos de 
    clientes y las comandas que se hacen en unas franjas horarias.

    Attributes
    ----------
    data : dict
        Datos las visitas al bar de distintos tipos de clientes y las comandas 
        que se hacen en unas franjas horarias.

    Methods
    -------
    add_visit(client_type, time)
        Añade una visita a la propiedad Data en la franja horaria que le corresponda.
    add_product_consumed(client_type, time)
        Añade una visita a la propiedad Data en la franja horaria que le corresponda.
    """

    def __init__(self):
        """
        Constructor de la entidad
        """

        self.data = {}


    def add_visit(self, client_type: str, time: int = None):
        """
        Añade una visita a la propiedad Data en la franja horaria que le corresponda.
        Si el tipo de cliente introducido no existe lanzará una excepción.
        Si la hora introducida aún no tiene valor se creará el par clave valor dentro
        de la propiedad data.
        Si no se le pasa parámetro de tiempo se utilizará la hora de inserción.

        Parameters
        ----------
        client_type : str
            Tipo de cliente que ha visitado el bar
        time : int
            Hora en la que se ha producido la visita.

        Returns
        -------
        None
        """
        
        clients_type = ["ninio", "joven", "adulto", "anciano"]
        if (client_type in clients_type) == False:
            raise AttributeError("El tipo de cliente especificado no es correcto.")
        elif time < 0 or time > 23:
            raise AttributeError("La hora especificado no es correcta.")
        elif time == None:
            hour = "%s:00" % (datetime.now.hour)
        elif time < 10:
            hour = "0%s:00" % (time)
        else:
            hour = "%s:00" % (time)

        self.initialize_hour(hour)

        self.data[hour]["clients_type"][client_type] += 1


    def add_product_consumed(self, product: str, time: int = None):
        """
        Añade un producto consumido a la propiedad Data en la franja horaria que le corresponda.
        Si la hora introducida aún no tiene valor se creará el par clave valor dentro
        de la propiedad data.
        Si no se le pasa parámetro de tiempo se utilizará la hora de inserción.

        Parameters
        ----------
        product : str
            Nombre del producto que se ha consumido.
        time : int
            Hora en la que se ha consumido el producto.

        Returns
        -------
        None
        """

        if time < 0 or time > 23:
            raise AttributeError("La hora especificado no es correcta.")
        elif time == None:
            hour = "%s:00" % (datetime.now.hour)
        elif time < 10:
            hour = "0%s:00" % (time)
        else:
            hour = "%s:00" % (time)

        self.initialize_hour(hour)

        if product in self.data[hour]["products_consumed"]:
            self.data[hour]["products_consumed"][product] += 1
        else:
            self.data[hour]["products_consumed"][product] = 1


    def initialize_hour(self, hour: str):
        """
        Método para inicializar una hora en la propiedad data.
        Si ya existe en el diccionario no hace nada.

        Parameters
        ----------
        hour : str
            Hora a inicializar.

        Returns
        -------
        None

        """
        if hour not in self.data:
            self.data[hour] = {
                "clients_type" : {
                    "ninio" : 0,
                    "joven" : 0,
                    "adulto" : 0,
                    "anciano" : 0,
                },
                "products_consumed" : {}
            }
        


