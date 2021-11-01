from dataclasses import dataclass

@dataclass(frozen=True)     # Cualquier asignación producirá una excepción
class Visit:                # del tipo dataclasses.FrozenInstanceError
    """
    Objeto valor que almacenará los datos relativos a una visita. Esta 
    clase será inmutable y su ciclo de vida dependerá de la clase Visits 

    Attributes
    ----------
    time: datetime
        Hora en la que se realiza la visita 
    type_user : str
        Tipo de cliente que ha realizado la visita.
    """
    time: int
    client_type: str
