from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre
    
    @abstractmethod
    def establecerNombre(self, nombre):
        self._nombre = nombre
        
    def obtenerNombre(self):
        return self._nombre
    
    def obtenerId(self):
        return self._id

    
    def equals(self, e):
        if isinstance(e, EntidadVineria):
            return self._id == e.obtenerId()
        else:
            return False