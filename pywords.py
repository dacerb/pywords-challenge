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
            insert_to_db(wordsCount, fileName)
    except Exception as e:
        print(mark+"get_collection_in_format : {}".format(e))
       
## Deberia subir a la BASE MONGO    
def insert_to_db(wordsCount, fileName):
    try:
        print(fileName)
        print(wordsCount)
    except Exception as e:
        print(mark+"insert_to_db: {}".format(e))
        

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
    path = config.path
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