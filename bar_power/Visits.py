from datetime import datetime
from bar_power.Order import *
from bar_power.Visit import *
from bar_power.ClientType import *

class Visits:
    """
    Entidad para almacenar la información sobre las visitas
    al bar de distintos tipos de clientes y las comandas que se
    hacen en unas franjas horarias.

    Attributes
    ----------
    data : dict
        Resumen global de las visitas que se van realizando a lo largo del día
        por los clientes: tramos horarios, tipos de clientes y productos
    v_visits: list of Visit
        Lista de objetos tipo Visit donde se almacenarán las horas de las visitas
        y el tipo de cliente que las realiza
    v_orders: list of Command
        Lista de objetos tipo Order donde se almacenarán las comandas que piden 
        los usuarios junto con las horas a las que se realizan

    Methods
    -------
    add_visit(client_type, time)
        Añade una visita a la propiedad Data en la franja horaria que le
         corresponda
    add_product_consumed(client_type, time)
        Añade una visita a la propiedad Data en la franja horaria que le
        corresponda
    """

    def __init__(self):
        """
        Constructor de la entidad
        """

        self.data = {}
        self.v_visits = []
        self.v_orders = []

    def add_visit(self, client_type: ClientType, time: int = None):
        """
        Añade una visita a la propiedad Data en la franja horaria que le
        corresponda.
        Si el tipo de cliente introducido no existe lanzará una excepción.
        Si la hora introducida aún no tiene valor se creará el par clave
        valor dentro de la propiedad data.
        Si no se le pasa parámetro de tiempo se utilizará la hora de inserción.

        Parameters
        ----------
        client_type : ClientType
            Tipo de cliente que ha visitado el bar
        time : int
            Hora en la que se ha producido la visita.

        Returns
        -------
        None
        """
        if type(client_type) != ClientType:
            raise AttributeError("El tipo de cliente especificado no es correcto.")

        hour = self.get_hour_from_time(time)

        self.initialize_hour(hour)

        self.data[hour]["clients_type"][client_type] += 1

        self.add_visit_done(hour, client_type)

    def add_product_consumed(self, product: str, time: int = None):
        """
        Añade un producto consumido a la propiedad Data en la franja horaria
        que le corresponda.
        Si la hora introducida aún no tiene valor se creará el par clave
        valor dentro de la propiedad data.
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
        
        hour = self.get_hour_from_time(time)

        self.initialize_hour(hour)

        if product in self.data[hour]["products_consumed"]:
            self.data[hour]["products_consumed"][product] += 1
        else:
            self.data[hour]["products_consumed"][product] = 1

        self.add_order_done(hour, product)

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
                "clients_type": {
                    ClientType.ninio: 0,
                    ClientType.joven: 0,
                    ClientType.adulto: 0,
                    ClientType.anciano: 0,
                },
                "products_consumed": {}
            }

    def add_visit_done(self, hour: int, client_type: ClientType):
        """
        Añade una visita a las visitas realizadas

        Parameters
        ----------
        hour : str
            Hora en la que llega el cliente
        client_type : ClientType
            Tipo de cliente
        """
        visit = Visit(hour, client_type)
        self.v_visits.append(visit)

    def add_order_done(self, hour: int, product: str):
        """
        Añade una producto a las comandas realizadas

        Parameters
        ----------
        hour : str
            Hora en la que se realiza el pedido
        product : str
            Producto consumido
        """
        order = Order(hour, product)
        self.v_orders.append(order)

    @staticmethod
    def get_hour_from_time(time):
        """
        Obtiene la hora en formato string del argumento pasado por parámetros.
        Si el parámetro time no es entero se usará la hora actual.

        Parameters
        ----------
        time : int
            Hora a transformar en string.

        Returns
        -------
        hour : str
            Hora en formato string obtenida.
        """

        if not isinstance(time, int):
            hour = "%s:00" % (datetime.now().hour)
        elif time < 0 or time > 23:
            raise AttributeError("La hora especificado no es correcta.")
        elif time < 10:
            hour = "0%s:00" % (time)
        else:
            hour = "%s:00" % (time)

        return hour

    def make_prediction(self,client_type: ClientType):
        """
        Este método hará una predicción haciendo uso del teorema de Bayes para 
        estimar la hora de llegada más probable del tipo de cliente pasado como
        parámetro

        Parameters
        ----------
        client_type: ClientType
            Tipo de cliente del que se quiere estimar la hora de llegada

        Returns
        --------
        hour: int
            Hora de llegada obtenida a partir de la predicción
        """
        pass
        
    def products_more_consumed(self):
        """
        Este método permite saber cuales son los productos más y menos 
        consumidos en función del cliente. Hará uso de los vectores v_visits 
        y v_orders para hacer una asociación entre los elementos de los arrays

        Returns
        --------
        m: matriz de str (4 x (num_productos))
            Matriz con 4 filas (una por cada tipo de cliente) donde cada
            una tendrá los productos ordenados de menos a más consumidos 
            según el tipo de cliente.
        """
        pass