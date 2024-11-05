import json
from entidadvineria import EntidadVineria
import vinoteca

class Cepa(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
    
    def establecerNombre(self, nombre):
        super().establecerNombre(nombre)
                
    def obtenerVinos(self):
        return [vino for vino in vinoteca.Vinoteca.obtenerVinos() if self in vino.obtenerCepas()]

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre() + " ("+ a.obtenerBodega().obtenerNombre()+ ")", vinos)
        return list(vinosMapa)