#Librerias
from pymongo import MongoClient

class Database():
    def __init__(self):
        self.__uri = "mongodb://31.97.102.106:27017"
        self.__cliente = MongoClient(self.__uri)
        #Usar la base de datos
        self.__db = self.__cliente['DiegoTech']
        #Coleccion
        self.__collection = None

    def insertar(self, documento, collection):
        self.__collection = self.__db[collection]
        resultado = self.__collection.insert_one(documento)
        print("Se realizo con exito la insercion de datos")
        
    def buscar(self, documento, collection):
        self.__collection = self.__db[collection]
        resultado = self.__collection.find(documento)
        print("Los resultados de tu consulta son:", resultado)

    def actualizar(self, docuemto, collection):
        self.__collection = self.__db[collection]
        self.__collection.update_one(docuemto)
        print("Los datos se atualizaron correctamente")