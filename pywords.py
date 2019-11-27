# -*- coding: utf-8 -*-

import config



### Error general en Execptions
mark=" [Error:]  "


## Devuelve arreglo de la cantidad de archivos para analizar
def get_files_collection(path):
    try:
        from os import listdir
        return  listdir(path)
    except Exception as e:
        print(mark+"get_collection_in_format : {}".format(e))



## Por cada archivo/colecion orquesto el procesamiento
def processing_files(filesNames, path):
    try:
        for fileName in filesNames:
            get_collection_in_format(path, fileName)
    except Exception as e:
        print(mark+"processing_files: {}".format(e))


## Procesa archivo/colecion recibida bajo nombre y path
def get_collection_in_format(path, fileName):
    try:  
        from collections import Counter
        with open(path+fileName) as collection:
            words = collection.read().split()
            wordsCount = Counter(words)
            #insert_to_db(wordsCount, fileName)
            construc_document(wordsCount, fileName)
    except Exception as e:
        print(mark+"get_collection_in_format : {}".format(e))


## Construyo el documento
def construc_document(wordsCount, fileName):
    try:

        import ast 
        ## La famosa magic adapto el documento para poder insertarlo a mongoDB
        magic=""
        document="{'name': '"+ fileName +"', 'words': {"
        for key, value in wordsCount.items():
                document += "{2} '{0}': {1}".format(key.replace(".", ""), value, magic)
                magic=","
        document +="}}"
        #Convierto String en diccionario
        document = ast.literal_eval(document)
        insert_to_db(document ,fileName )
    except Exception as e:
        print(mark+"construc_document: {} -- {}".format(e,fileName))
        print(document)
        input()
        



## Deberia subir a la BASE MONGO    
def insert_to_db(document,fileName):
    try:
        from pymongo import MongoClient
        ## Definimos el objeto para la conexion con la base de mongo
        connection 	= MongoClient(config.MONGO_HOST, config.MONGO_PORT)
        db 			= connection[config.MONGO_DB]
        collection	=db[config.MONGO_COLLECTION]
        auth_mongo = collection#.authenticate(config.MONGO_USER, config.MONGO_PASS)

        #print(type(document))
        auth_mongo.insert(document)

    except Exception as e:
        print(mark+"insert_to_db: {} -- {}".format(e,fileName))
    

def get_time():
    try:
        from time import time
        chronometer = time()
        return chronometer
    except Exception as e:
        print(mark+"get_time: {}".format(e))
    

## Ejecucion principal del programa
def main():
    
    ## Ruta donde estan los archivos
    start_run = get_time()
    path = config.FILE_PATH
    try:
        filesNames = get_files_collection(path)
        processing_files(filesNames, path)
    
        ## Calculo y muestro tiempo de ejecucion
        elapsed_time = get_time() - start_run
        print("\n\nElapsed time: {} seconds.".format(elapsed_time))
    except Exception as e:
        print(mark+"main: {}".format(e))

    print("Push anykey for exit")
    input()
 

## Atrapa la ejecucion interna __main__ de python para ordejar la ejecucion.
if __name__ == '__main__':
    
    main()