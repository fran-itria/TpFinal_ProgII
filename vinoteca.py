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

    def buscarBodega(id):
        for bodega in Vinoteca.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None
        
    def buscarCepa(id):
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None
    
    def buscarVino(id):
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None
    
    def __convertirJsonAListas(lista):
        for item in lista:
            if item['tipo'] == 'bodega':
                Vinoteca.__bodegas.append(Bodega(item['id'], item['nombre']))
            elif item['tipo'] == 'cepa':
                Vinoteca.__cepas.append(Cepa(item['id'], item['nombre']))
            elif item['tipo'] == 'vino':
                Vinoteca.__vinos.append(Vino(item['id'], item['nombre'], item['bodega'], item['cepas'], item['partidas']))
    
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