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

    def obtenerBodegas(orden=None, reverso=False) -> list[Bodega]:
        if isinstance(orden, str):
            if orden == "nombre":
                return sorted(Vinoteca.__bodegas, key=lambda b: b.obtenerNombre(), reverse=reverso)
            elif orden == "vinos":
                return sorted(Vinoteca.__bodegas, key=lambda b: len(b.obtenerVinos()), reverse=reverso)
        return Vinoteca.__bodegas.copy()
    
    def obtenerCepas(orden=None, reverso=False) -> list[Cepa]:
        if isinstance(orden, str):
            if orden == "nombre":
                return sorted(Vinoteca.__cepas, key=lambda c: c.obtenerNombre(), reverse=reverso)
        return Vinoteca.__cepas.copy()
    
    def obtenerVinos(anio=None, orden=None, reverso=False) -> list[Vino]:
        vinos = Vinoteca.__vinos
        if isinstance(anio, int):
            vinos = [vino for vino in vinos if anio in vino.obtenerPartidas()]
        if isinstance(orden, str):
            if orden == "nombre":
                vinos = sorted(vinos, key=lambda v: v.obtenerNombre(), reverse=reverso)
            elif orden == "bodega":
                vinos = sorted(vinos, key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso)
            elif orden == "cepas":
                return sorted(vinos, key=lambda v: len(v.obtenerCepas()), reverse=reverso)
        return vinos
    
    def buscarBodega(id) -> Bodega:
        for bodega in Vinoteca.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None
        
    def buscarCepa(id) -> Cepa:
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None
    
    def buscarVino(id) -> Vino:
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None
    
    @staticmethod
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