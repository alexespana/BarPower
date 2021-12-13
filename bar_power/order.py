from dataclasses import dataclass

@dataclass(frozen=True)     # Cualquier asignación producirá una excepción
class Order:                # del tipo dataclasses.FrozenInstanceError
    """
    Objeto valor que almacenará los datos relativos a una comanda. Esta 
    clase será inmutable y su ciclo de vida dependerá de la clase Visits 

    Attributes
    ----------
    time: datetime
        Hora en la que se realiza la comanda 
    product_consumed : str
        Producto que pide el cliente en la visita.
    """
    time: int
    product: str
