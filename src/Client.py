from datetime import datetime

class Client:
    """
    Entidad para almacenar los datos de los clientes de la aplicación.

    Attributes
    ----------
    age : int
        Edad del cliente.
    region : str
        Procedencia del cliente.
    visits : dict of {str : datetime}
        Visitas del cliente a un bar y a una hora determinada.
    products_consumed : dict of {str : int}
        Productos consumidos por el cliente junto con la cantidad de veces consumido cada producto.

    Methods
    -------
    get_age()
        Obtiene la propiedadd Edad de la entidad.
    set_age(age)
        Establece la propiedad Edad de la entidad.
    get_visits()
        Obtiene la propiedad Visitas de la entidad.
    get_products_consumed()
        Obtiene la propiedad Productos Consumidos de la entidad.
    add_visit(bar, date = None)
        Añade una visita a un bar en una fecha determinada a la propiedad Visitas de la clase.
    add_product_consumed(product)
        Añade un producto consumido a la propiedad Productos consumidos.
    check_age(age)
        Comprueba que la edad pasada por parámetros es correcta.
    """

    def __init__(self, age, region):
        """
        Construye todos los atributos necesarios para la entidad

        Parameters
        ----------
        age : int
            Edad del cliente.
        regiosn : str
            Procedencia del cliente.
        visits : dict of {str : datetime}
            Visitas los bares y a una hora determinada del cliente.
        products_consumed : dict of {str : int}
            Productos consumidos junto a la cantidad por el cliente.
        """

        Client.check_age(age)
        self.age = age
        self.region = region
        self.visits = []
        self.products_consumed = []


    def get_age(self):
        """
        Obtiene la edad del cliente.

        Returns
        -------
        int
            Edad del cliente.
        """
        return self.age

    def set_age(self, age):
        """
        Establece la edad del cliente.

        Parameters
        ----------
        age : int
            Edad del cliente a establecer.

        Returns
        -------
        None
        """

        Client.check_age(age)
        self.age = age

    def get_visits(self):
        """
        Obtiene las visitas realizadas por el cliente.

        Returns
        -------
        dict of {str : datetime}
            Visitas a los bares a una hora determinada del cliente.
        """
        return self.visits

    def get_products_consumed(self):
        """
        Obtiene los productos consumidos por el cliente.

        Returns
        -------
        dict of {str : int}
            Productos consumidos junto a la cantidad por el cliente.
        """
        return self.products_consumed


    @staticmethod
    def check_age(age):
        """
        Comprueba que la edad sea un valor correcto.
        Si el valor no es un entero y no está entre 3 y 100 lanza una excepción.

        Parameters
        ----------
        age : int
            Edad a checkear.

        Returns
        -------
        None
        """
        if not isinstance(age, int) or age < 3 or age > 100:
            raise AttributeError("La edad para asignar al cliente no es correcta.")
