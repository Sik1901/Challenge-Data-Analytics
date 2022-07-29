import download
import connect
from concurrent.futures import process
from logging.config import logging as log
from utils import *
from Scripts import descargar_csv, modificar_datos, cargar_tablas
from Urls import Url_Biblotecas, Url_Cines, Url_Museos


log.info('Descargando archivos fuente')

descargar_csv(Url_Biblotecas, 'bibliotecas')
descargar_csv(Url_Museos, 'museos')
descargar_csv(Url_Cines, 'cines')

log.info('Procesando datos y creando tablas')
modificar_datos()

log.info('Conectando con base de datos y subiendo tablas')
cargar_tablas()

log.info('Ejecución finalizada con éxito')