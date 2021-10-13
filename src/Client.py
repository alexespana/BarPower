from datetime import datetime

class Client:

    # Constructor por parámetros de la entidad.
    def __init__(self, age, region):
        Client.check_age(age)
        self.age = age
        self.region = region
        self.visits = []
        self.products_consumed = []


    # Obtiene la propiedad Age de la entidad.
    def get_age(self):
        return self.age

    # Establece la propiedad Age de la entidad.
    def set_age(self, age):
        Client.check_age(age)
        self.age = age

    # Obtiene la propiedad Visitas de la clase.
    def get_visits(self):
        return self.visits

    # Obtiene la propiedad Productos Consumidos de la clase.
    def get_products_consumed(self):
        return self.products_consumed


    # Añade una visita a un bar en una fecha determinada a la propiedad Visitas de la clase.
    # Si no se introduce ninguna fecha utilizará la fecha actual de inserción.
    def add_visit(self, bar, date = None):
        if date == None:
            date = datetime.now()

        self.visits[date] = bar

    # Añade un producto consumido a la propiedad Productos consumidos.
    def add_product_consumed(self, product):
        if product in self.products_consumed:
            self.products_consumed[product] += 1
        else:
            self.products_consumed[product] = 1


    # Método para comprobar que la edad del cliente es correcta.
    @staticmethod
    def check_age(age):
        if not isinstance(age, int) or age < 3 or age > 100:
            raise AttributeError("La edad para asignar al cliente no es correcta.")
