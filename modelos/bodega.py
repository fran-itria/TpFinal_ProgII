import json
from entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        
    def establecerNombre(self, nombre):
        super().establecerNombre(nombre)
                
    def obtenerVinos(self):
        from vinoteca import Vinoteca
        vinosTodos = Vinoteca.obtenerVinos()
        vinos = [vino for vino in vinosTodos if self._id == vino.obtenerBodega()]
        return vinos
    
    def obtenerCepas(self):
        from vinoteca import Vinoteca
        vinosTodos = Vinoteca.obtenerVinos()
        vinos = [vino for vino in vinosTodos if self._id == vino.obtenerCepas()]
        return vinos

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)
