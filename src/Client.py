from datetime import datetime

class Client:

    # Constructor por parámetros de la entidad.
    def __init__(self, age, region):
        Client.check_age(age)
        self.age = age
        self.region = region
        self.visits = []


    # Obtiene la propiedad Age de la entidad.
    def get_age(self):
        return self.age

    # Establece la propiedad Age de la entidad.
    def set_age(self, age):
        Client.check_age(age)
        self.age = age

    # Obtiene la propiedad Region de la entidad.
    def get_region(self):
        return self.region

    # Establece la propiedad Region de la entidad.
    def set_region(self, region):
        self.region = region

    # Obtiene la propiedad Visitas de la clase.
    def get_visits(self):
        return self.visits


    # Añade una visita a un bar en una fecha determinada a la propiedad Visitas de la clase.
    # Si no se introduce ninguna fecha utilizará la fecha actual de inserción.
    def add_visit(self, bar, date = None):
        if date == None:
            date = datetime.now()

        self.visits[date] = bar


    # Método para comprobar que la edad del cliente es correcta.
    @staticmethod
    def check_age(age):
        if not isinstance(age, int) or age < 3 or age > 100:
            raise AttributeError("La edad para asignar al cliente no es correcta.")
