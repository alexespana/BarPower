class Client:

    # Constructor por parámetros de la entidad.
    def __init__(self, age, region):
        Client.check_age(age)
        self.age = age
        self.region = region


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


    # Método para comprobar que la edad del cliente es correcta.
    @staticmethod
    def check_age(age):
        if not isinstance(age, int) or age < 3 or age > 100:
            raise AttributeError("La edad para asignar al cliente no es correcta.")
