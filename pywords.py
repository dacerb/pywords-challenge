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


def order_top_ten_words(objeto_diccionario):
    
    try:
        import operator

        
        ## ordeno el con formato dict el diccionario de las 10 palabras mas usadas.
        objeto_diccionario_sort = dict(sorted(objeto_diccionario.items(), key=lambda x: x[1], reverse=True))

        ## Creo dos listas para almacenar los dalores por separados
        words_ranking = list()
        words_graph = list()
        for value , key in objeto_diccionario_sort.items():
            words_graph.append(value)
            words_ranking.append(key)

        return words_ranking , words_graph
    
    except Exception as e:
        print(mark+"order_top_ten_words: {}".format(e))


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
       
       # Defino el Objeto 
        document = {
            'name': fileName,
            'words': {},            
            'words_low_match':[],   ## ADD Field
            'words_qty':0           ## ADD Field
            
        }

        for key, value in wordsCount.items():   ## con la siguiente Comprehension 
            document['words'][key] = value      ## Recorro clave  agregando en el objto    
            document['words_qty'] += 1
            
            if value == 1 :
                document['words_low_match'].append(key)
            ##document['words'] = wordsCount    ## Opcion 2 de agregar el dict
        insert_to_db(document, fileName)  
        
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
    return conect_db().count_documents({}) ## Consulta a mejorar traer todo de una


def query_mongoDB_distinct_words():
    return conect_db().count_documents({}) ## Consulta a mejorar traer todo de una


def query_mongoDB_document_more_words():
    document_name = conect_db().find({},{'name':1,'_id':0}).sort([('words_qty',-1)]).limit(1)     ## Consulta a mejorar traer todo de una  OK
    document_name_get = dict(document_name[0])
    return document_name_get['name']


def query_top_ten_collection_words():
    document_name = conect_db().find_one({},{'words':1,'name':1, '_id':0})   ## Consulta a mejorar traer todo de una
    return document_name['words'] 
## Querys a Mongo DB###########################0

## consultar reloj
def get_time():
    try:
        from time import time
        chronometer = time()
        return chronometer
    except Exception as e:
        print(mark+"get_time: {}".format(e))

## mostrar grafico recibe (qty_documents,document_more_words,qty_distinct_words,top_ten_collection)
def pygraph_reports(qty_documents,document_more_words,qty_distinct_words,top_ten_collection_words,start_run):
    try:
        ## Me traigo los datos ordenados para armar el pie
        words_ranking , words_graph = order_top_ten_words(top_ten_collection_words)
        
        from matplotlib import pyplot as  plt

        ## Tuplas necesarias para graficar
        words       = words_graph[:10]    ## Se agrega la lista procesada y limito de [0:10] 
        slicesWords = words_ranking[:10]  ## Se agrega la lista procesada y limito de [0:10] 
        valuesWords = (0.06,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0) ## Podria generarlo con una funcion
        sliceColorWords = ('#FFE800','#DFCD15','#C2B424','#9B912E','#817A32','#605C32','#504E34','#3C3B2E','#292925','#000000')
       
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
        elapsed_time = get_time() - start_run
        print("\n\nElapsed time: {} seconds --> Execution time".format(elapsed_time))
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
        top_ten_collection_words  = query_top_ten_collection_words()

        ## Generar reporte grafico
        pygraph_reports(qty_documents,document_more_words,qty_distinct_words,top_ten_collection_words,start_run)
        
   
        ## Calculo y muestro tiempo de ejecucion
        elapsed_time = get_time() - start_run
        print("Elapsed time: {} seconds --> Exit pywords\n\n".format(elapsed_time))
    except Exception as e:
        print(mark+"main: {}".format(e))

 

## Atrapa la ejecucion interna __main__ de python para ordejar la ejecucion.
if __name__ == '__main__':
    
    main()