# -*- coding: utf-8 -*-
__author__ = 'David Acerbo'

import codecs
import re
import config
from pymongo import MongoClient

### Error general en Execptions
mark=" [Error:]  "

## Funcion para conectar se puede mejorar para pasar base y coleccion como parametros 
def conect_db():
    try:
        from pymongo import MongoClient

        client = MongoClient(config.MONGO_HOST, config.MONGO_PORT)
        client.admin.authenticate(config.MONGO_USER, config.MONGO_PASS, mechanism = 'SCRAM-SHA-1', source=config.MONGO_DB)
        db_name = client[config.MONGO_DB]
        collection_name = config.MONGO_COLLECTION
        conection = db_name[collection_name]
        
        return conection 
        
    except Exception as e:
        print(mark+"conect_db: {}".format(e))


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


## Procesa archivo/colecion recibida bajo path y fileName
def get_collection_in_format(path, fileName):
    try:  
        from collections import Counter
        with codecs.open(path+fileName, encoding='utf8') as collection:   ## uso el codecs utf8 para ordernar la salida
            words = collection.read()
            words_split = re.sub('([0-9]+)|([\W_]+)', ' ',words ).split() ## Saco caracteres Match y corto las palabras
            wordsCount = Counter(words_split) #cuento palabras
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


## Deberia subir a la BASE MONGO    
def insert_to_db(document,fileName):
    try:
        conect_db().insert_one(document)         
    except Exception as e:
        print(mark+"insert_to_db: {} -- {}".format(e,fileName))


## Querys a Mongo DB###########################
def query_mongoDB_count_document():
    return conect_db().count_documents({})


def query_mongoDB_distinct_words():
    return conect_db().count_documents({})


def query_mongoDB_document_more_words():
    return conect_db().count_documents({})


def query_top_ten_collection():
    return {('Hola','Casa','Perro','GO','La','queso','mono','zorro','GOy','Laa')}
## ^^ Querys a Mongo DB###########################

## consultar reloj
def get_time():
    try:
        from time import time
        chronometer = time()
        return chronometer
    except Exception as e:
        print(mark+"get_time: {}".format(e))

## mostrar grafico recibe (qty_documents,document_more_words,qty_distinct_words,top_ten_collection)
def pygraph_reports(qty_documents,document_more_words,qty_distinct_words,top_ten_collectio):
    try:
        from matplotlib import pyplot as  plt

        ## Tuplas necesarias para graficar
        words = top_ten_collectio                         ## Se agrega con el objeto 
        slicesWords = (100,90,87,80,70,50,30,25,22,10)    ## Se agrega con el objeto 
        valuesWords = (0.06,0,0,0,0,0,0,0,0,0) ## Podria generarlo con una funcion
       
        ## Datos para caja de texto
        distinct_words = qty_distinct_words
        documents_qty = qty_documents
        document_whit_more_words = document_more_words
       
        ## Caja de texto
        text_box='\n\n Palabras Diferentes:\n > '+str(distinct_words)
        text_box +='\n\n Documentos Totales:\n > '+str(documents_qty)
        text_box +='\n\n Documento con mas palabras:\n > '+str(document_whit_more_words)+'\n\n' 

        ## Ocultar Toolbar
        plt.rcParams['toolbar']='None'

        ## defino la figura
        fig = plt.figure(0, figsize=(20,10))
        ax = fig.add_subplot(111)
      
        ## defino el titulo general
        plt.title('TOP 10 DE PALABRAS EN LA COLECCIÓN \n\n' , weight='bold' ,verticalalignment='center',fontsize=20 )
       
        ## defino el modo como se dibuja el grafico
        ax.axis('equal')
        sliceColorWords = ('#FFE800','#DFCD15','#C2B424','#9B912E','#817A32','#605C32','#504E34','#3C3B2E','#292925','#000000')
        _, _, graph_text = ax.pie(slicesWords,
                    colors=sliceColorWords,
                    labels=words,
                    autopct='%1.1f%%', ## Procentage y su formato del porcentage
                    explode=valuesWords,
                    startangle=90, ## Angulo
                    )
        ax.pie

        ## Recoremos Los textos para setiarlos en blanco
        for text in graph_text:
            text.set_color('white')
        

        ## Agrego caja de texto, con resultado de las querys
        y = 0.7
        x = -2.4
        plt.text(x, y, text_box, color='white', weight='bold', horizontalalignment='left', verticalalignment='center', bbox=dict(facecolor='#000000', alpha=0.9 ,boxstyle='round', edgecolor='#3C3B2E', pad=1) )

        ## mustro pyplot que contiene todo los parametros ya cargados.
        plt.show()

    except Exception as e:
        print(mark+"pygraph_reports: {}".format(e))


## Ejecucion principal del programa
def main():
    
    ## Ruta donde estan los archivos
    start_run = get_time()
    path = config.FILE_PATH
    try:
        filesNames = get_files_collection(path)
        processing_files(filesNames, path)
   
        ### Realizo consultas para luego pasar a pygraph
        qty_documents = query_mongoDB_count_document()
        qty_distinct_words  = query_mongoDB_distinct_words()
        document_more_words = query_mongoDB_document_more_words()
     
        ##top_ten_collection  = query_top_ten_collection()
        top_ten_collection  = ('pywords2','vuelvoloco','mas','menos','mona','chinverguencha','mono','zorro','GOy','Laa')

        ## Generar reporte grafico
        pygraph_reports(qty_documents,document_more_words,qty_distinct_words,top_ten_collection)
        
   
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