#import config
import re
##import pywords
##from pymongo import MongoClient
#from pymongo import MongoClient
#
#
### Definimos el objeto para la conexion con la base de mongo
#connection 	= MongoClient(config.MONGO_HOST, config.MONGO_PORT)
#db 			= connection[config.MONGO_DB]
#collection	=db[config.MONGO_COLLECTION]
#auth_mongo = collection #.authenticate(config.MONGO_USER, config.MONGO_PASS)


#print(auth_mongo)

#result = pywords.main()

#print(result)

#primero = {"name": "textpo-txt"}
#diccionario = {'Y': 2, 'LA': 1, 'VIDA': 1, 'LAZARILLO': 1, 'TORMES': 1, 'SUS': 1, 'FORTUNAS': 1, 'ADVERSIDADES': 1, 'Autor': 1, 'desconocido': 1, 'Edición': 1, 'de': 1, 'Burgos,': 1, '1554': 1}
#
#txt="({'name': 'files.txt'"
#for clave, valor in diccionario.items():
#    txt += ", {}: {}".format(clave, valor)
#txt +="})"
#
#print(txt)
#res = diccionario.values

#print(res)

#print(primero + diccionario)

#auth_mongo.insert({'name': '123133333.txt', 'words': { 'LA': 1, 'VIDA': 1, 'Dêeëqwe,': 3, 'LAZARILLO': 1, 'TORMES': 1, 'Y': 2, 'SUS': 1, 'FORTUNAS': 1, 'ADVERSIDADES': 1, 'Autor': 1, 'desconocido': 1, 'Edición': 1, 'de': 1, 'Burgos': 1, '1554': 1}})
#auth_mongo.insert({'name': '1axeellasd31.txt', 'words': { 'LA': 1, 'VIDA': 1, 'DE': 3, 'LAZARILLO': 1, 'TORMES': 1, 'Y': 2, 'SUS': 1, 'FORTUNAS': 1, 'ADVERSIDADES': 1, 'Autor': 1, 'desconocido': 1, 'Edición': 1, 'de': 1, 'Burgos,': 1, '1554': 1}})
#auth_mongo.insert({'name': 'dddasaaa.txt', 'words': { 'LA': 1, 'VIDA': 1, 'DE': 3, 'LAZARILLO': 1, 'TORMES': 1, 'Y': 2, 'SUS': 1, 'FORTUNAS': 1, 'ADVERSIDADES': 1, 'Autor': 1, 'desconocido': 1, 'Edición': 1, 'de': 1, 'Burgos,': 1, '1554': 1}})


#ef construc_document(wordsCount, fileName):
#   try:
#       ## La famosa magic adapto el documento para poder insertarlo a mongoDB
#       magic=""
#       document="({'name': '"+ fileName +"', 'words': {"
#       for key, value in wordsCount.items():
#               document += "{2} '{0}': {1}".format(key.replace(".", ""), value, magic)
#               magic=","
#       document +="}})"
#       print(document)
#       insert_to_db(document)
#   except Exception as e:
#       print(mark+"construc_document: {}".format(e))
#

#({'name': 'dddasaaa.txt', 'words': { 'LA': 1, 'VIDA': 1, 'DE': 3, 'LAZARILLO': 1}})


#numbers1 = dict([('x', 5), ('y', -5)])
#numbers1 += dict([('x', 5), ('y', -5)])
#numbers1 += dict([('x', 5), ('y', -5)])
#print('numbers1 =',numbers1)

y="<font x=''>test</font> <font y=''>test2</font> <font z=''>test3</font>"
x=re.findall(r"(?<=>)([^<]*)(?=<\/)",y) 
str=" ".join(x)
print(str) 

#######################
#class Complejo:
#     def __init__(self, partereal, parteimaginaria):
#         self.r = partereal
#         self.i = parteimaginaria
#
#x = Complejo(3.0, 23123)
##print(x.r, x.i)
#
#diccion={x.r , x.i}
#print(diccion)
#######################


input()
