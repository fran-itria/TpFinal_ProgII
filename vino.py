import json
from entidadvineria import EntidadVineria
from vinoteca import Vinoteca



class Vino(EntidadVineria):
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas
        
    def establecerBodega(self, bodega):
        self.__bodega = bodega
        
    def establecerCepas(self, cepas):
        self.__cepas = cepas
        
    def establecerPartidas(self, partidas):
        self.__partidas = partidas
        
    def obtenerBodega(self):
        return Vinoteca.buscarBodega(self.__id)

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
