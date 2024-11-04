import json
from entidadvineria import EntidadVineria

class Cepa(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
    
    def establecerNombre(self, nombre):
        super().establecerNombre(nombre)
                
    def obtenerVinos(self):
        from vinoteca import Vinoteca
        vinosTodos = Vinoteca.obtenerVinos()
        vinos = [vino for vino in vinosTodos if self._id == vino.obtenerCepas()]
        return vinos
        

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
