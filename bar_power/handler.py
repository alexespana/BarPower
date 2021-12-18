import logging

from bar_power.visit import Visit
from bar_power.order import Order
from bar_power.visits import Visits
from bar_power.clientType import ClientType
from bar_power.logger import Logger

class Handler:
    
    def __init__(self):
        self.logger = Logger()
        self.visit : Visit
        self.order : Order
        self.visits : Visits

    def create_visit(self, time: int, client_type: ClientType):
        try:
            self.visit = Visit(time, client_type)
            self.logger.info("La visita ha sido creada correctamente")
            return self.visit
        except Exception as exception:
            self.logger.error("Hubo un error al intentar crear la visita")
            raise exception

    def create_order(self, time: int, product: str):
        try:
            self.order = Order(time, product)
            self.logger.info("La comanda ha sido creada correctamente")
            return self.order
        except Exception as exception:
            self.logger.error("Hubo un error al intentar crear la comanda")
            raise exception

    def create_visits(self):
        try:
            self.visits = Visits()
            self.logger.info("El vector de visitas ha sido creado correctamente")
            return self.visits
        except Exception as exception:
            self.logger.error("Hubo un error al intentar crear el vector de visitas")
            raise exception

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
        try:
            self.visits.add_visit(client_type, time)
            self.logger.info("Se ha registrado una nueva visita al local")
        except Exception as exception:
            self.logger.error(print(exception))
            raise exception

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
        try:
            self.visits.add_product_consumed(product, time)
            self.logger.info("Se ha registrado la comanda de " + product + " correctamente")
        except Exception as exception:
            self.logger.error(print(exception))
            raise exception   
