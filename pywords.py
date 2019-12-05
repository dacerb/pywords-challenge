# -*- coding: utf-8 -*-
__author__ = 'David Acerbo'

import codecs
import re
import config
import operator
from pymongo import MongoClient
from collections import Counter , defaultdict
from matplotlib import pyplot as  plt

### Error general en Execptions
mark=" [Error:]  "


## Funcion para conectar se puede mejorar para pasar base y coleccion como parametros 
def conect_db():
    try:
       
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
            'words': {}            
            
        }

        for key, value in wordsCount.items():   ## con la siguiente Comprehension 
            document['words'][key] = value      ## Recorro clave  agregando en el objto    
        
        insert_to_db(document, fileName)        ## Mando a insertar la base de datos 
        
    except Exception as e:
        print(mark+"construc_document: {} -- {}".format(e,fileName))


## Deberia subir a la BASE MONGO    
def insert_to_db(document,fileName):
    try:
        conect_db().insert_one(document)         
    except Exception as e:
        print(mark+"insert_to_db: {} -- {}".format(e,fileName))


## consulta a mongo cantidad de documentos
def query_mongoDB_count_document():
    qty_documents = conect_db().count_documents({})
    
    return qty_documents 


## descarga los documentos de mongo, y procesa en moria haciendo merge de los diccionarios y durante el proceso encuentra el documento con mayor cantidad de palabras.
def query_mongodb_object_document():    
    
    
    try:
        
        aux_qty_document = 0
        obtain_document_name = ""
        dictionary_total = defaultdict(int)
        query_get_documents_db = conect_db().find({},{'name': 1, 'words': 1})
        
        for doc in query_get_documents_db:
            
            get_document_name        = doc['name']  ## Almaceno los nombres por documento recorrido
            get_document_dictionary  = doc['words'] ## Almaceno los dict por documento recorrido
            dictionary_total  = merge_dicts(dictionary_total , get_document_dictionary) ## Sumo palabras de todos los documentos agregando e incrementando segun fuera el caso
            
            get_document_qty  = count_dictionary_dimension(get_document_dictionary)  ## Cuento palabras sin tener en cuenta la repeticion tengo que mejorar IMPORTANTE !!!
            ## aprovecho la recursividad para ir validando que documento tiene mas palabras
            if aux_qty_document <= get_document_qty :
                aux_qty_document = get_document_qty
                obtain_document_name = get_document_name            
                
        ## Devuelvo String nombre del documento con mas palabras, merge de todos los diccionarios agregando no existentes y sumando palabras existentes    
        ##           document_more_words , top_ten_collection_words
        return       obtain_document_name ,  dictionary_total
   
    except Exception as e:
        print(mark+"query_mongoDB_count_document: {}".format(e))    


## Suma diccionarios si hay palabras repetidas y agrega las que no.
def merge_dicts(dictionary_total, get_document_dictionary):
    
    try: 
        dictionary_total = { key: dictionary_total.get(key, 0) + get_document_dictionary.get(key, 0) for key in set(dictionary_total) | set(get_document_dictionary) }
        return dictionary_total ## retorno suma de dos diccionarios, el total mas el iterante 
    except Exception as e:
        print(mark+"merge_dicts: {}".format(e))
    

## cuenta la dimension de elementos que contiene el directorio 
def count_dictionary_dimension(get_document_dictionary):

    try:
        words_qty = 0
        for  value in get_document_dictionary.values():
            words_qty = words_qty + value
            
        return words_qty

    except Exception as e:
        print(mark+"count_dict_dimension: {}".format(e))


## Ordena y recorre por los valores que indican la repeticion de la palabra donde 1 indica que solo aparece una ves 
## lo que lo hace distinta
def search_distinct_words_dictionary(dictionary_total):
    
    objeto_diccionario_sort = dict(sorted(dictionary_total.items(), key=lambda x: x[1], reverse=False))
    
    qty_distinct_words = 0
    for value in objeto_diccionario_sort.values():
        
        if value == 1:
            qty_distinct_words += value
        else:
             break
         
    return qty_distinct_words
    

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
        print("Elapsed time: {} seconds --> pygraph_reports".format(elapsed_time))
        plt.show()

    except Exception as e:
        print(mark+"pygraph_reports: {}".format(e))


## Ejecucion principal del programa
def main():
    

    try:
        conect_db().drop() ## Borro la base para debug evitar funcionamientos inesperados al procesar los nuevos datos y los anteriores de la coleccion.
        
        ## Ruta donde estan los archivos
        start_run = get_time()
        path = config.FILE_PATH
         
        filesNames = get_files_collection(path)
        processing_files(filesNames, path)
        elapsed_time = get_time() - start_run    
        print("\n\nElapsed time: {} seconds --> processing_files".format(elapsed_time))
      
        ### Realizo consultas para luego pasar a pygraph
        qty_documents                            = query_mongoDB_count_document()
        obtain_document_name , dictionary_total  = query_mongodb_object_document()
        document_more_words                      = obtain_document_name ## Corregir para que este mas prolijo
        top_ten_collection_words                 = dictionary_total     ## Corregir para que este mas prolijo
        qty_distinct_words                       = search_distinct_words_dictionary(dictionary_total)
        
        elapsed_time = get_time() - start_run    
        print("Elapsed time: {} seconds --> query_mongodb".format(elapsed_time))
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