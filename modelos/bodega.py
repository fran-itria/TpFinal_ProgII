import json
from entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        
    def establecerNombre(self, nombre):
        super().establecerNombre(nombre)
                
    def obtenerVinos(self):
        from vinoteca import Vinoteca
        return [vino for vino in Vinoteca.obtenerVinos() if self._id == vino.obtenerBodega().obtenerId()]
    
    def obtenerCepas(self):
        from vinoteca import Vinoteca
        cepas = []
        for vino in Vinoteca.obtenerVinos():
            if self._id == vino.obtenerBodega().obtenerId():
                for cepa in vino.obtenerCepas():
                    if cepa not in cepas:
                        cepas.append(cepa)
        return cepas

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
