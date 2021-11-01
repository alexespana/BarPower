from datetime import datetime
import bar_power.Visit, bar_power.Order

class Visits:
    """
    Entidad para almacenar la información sobre las visitas
    al bar de distintos tipos de clientes y las comandas que se
    hacen en unas franjas horarias.

    Attributes
    ----------
    data : dict
        Datos las visitas al bar de distintos tipos de clientes y las comandas
        que se hacen en unas franjas horarias.
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

    def add_visit(self, client_type: str, time: int = None):
        """
        Añade una visita a la propiedad Data en la franja horaria que le
        corresponda.
        Si el tipo de cliente introducido no existe lanzará una excepción.
        Si la hora introducida aún no tiene valor se creará el par clave
        valor dentro de la propiedad data.
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
        if (client_type in clients_type) is False:
            raise AttributeError("El tipo de cliente especificado no \
                                  es correcto.")

        hour = self.get_hour_from_time(time)

        self.initialize_hour(hour)

        self.data[hour]["clients_type"][client_type] += 1

        self.v_visits.append(bar_power.Visit.Visit(hour, client_type))

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

        self.v_orders.append(bar_power.Order.Order(hour, product))
        
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
                    "ninio": 0,
                    "joven": 0,
                    "adulto": 0,
                    "anciano": 0,
                },
                "products_consumed": {}
            }

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

    def make_prediction(self,client_type):
        """
        Este método hará una predicción haciendo uso del teorema de Bayes para 
        estimar la hora de llegada más probable del tipo de cliente pasado como
        parámetro

        Parameters
        ----------
        client_type: str
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