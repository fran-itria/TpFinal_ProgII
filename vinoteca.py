# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    def obtenerBodegas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "vinos":
                pass  # completar
        pass  # completar

    def obtenerCepas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
        pass  # completar

    def obtenerVinos(anio=None, orden=None, reverso=False):
        if isinstance(anio, int):
            pass  # completar
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "bodega":
                pass  # completar
            elif orden == "cepas":
                pass  # completar
        pass  # completar

    def buscarBodega(self, id):
        for bodega in self.bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None
        
    def buscarCepa(self, id):
        for cepa in self.cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None
    
    def buscarVino(self, id):
        for vino in self.vinos:
            if vino.obtenerId() == id:
                return vino
        return None
    
    def __convertirJsonAListas(self, lista):
        for item in lista:
            if item['tipo'] == 'bodega':
                self.bodegas.append(item['nombre'])
            elif item['tipo'] == 'cepa':
                self.cepas.append(item['nombre'])
            elif item['tipo'] == 'vino':
                self.vinos.append(item['nombre'])

    def __parsearArchivoDeDatos():
        datos = {}
        if os.path.exists(Vinoteca.__archivoDeDatos):
            try:
                with open(Vinoteca.__archivoDeDatos, 'r') as archivo:
                    datos = json.load(archivo)
            except FileNotFoundError:
                print("El archivo no existe")
            except json.JSONDecodeError:
                print("El archivo no contiene datos JSON validos")
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
            else:
                print(f'El archivo "{Vinoteca.__archivoDeDatos}" se abrio y leyo correctamente')
        return datos