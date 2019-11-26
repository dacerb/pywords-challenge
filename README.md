# CHALLENGE MERCADO LIBRE 
Desarrolle un programa que le permita obtener los siguientes valores sobre la colección de documentos adjunta:

- Cantidad de palabras diferentes en la colección
- Cantidad de documentos
- Determinar cuál es el documento con más palabras

Utilizando una base de datos no relacional MongoDB almacene la frecuencia de las palabras por documento con la siguiente estructura:
```sh
[ {"doc_name" : "doc1",
  "words": {"devOps": 3, "challenge": 2 , "Meli": 4}},
 {"doc_name" : "doc2",
  "words": {"Python": 10, "Test": 1 , "words": 5}},
 {"doc_name" : "doc2", 
   "words": {"CoreServices": 1, "Test": 2 , "json": 20}}
]
```
#### ¿Que hace pywords.py ? 
    pywords.py arma una lista de las colecciones ubicadas en la ruta de configuracion cargada en config.py.
    Utilizando las funciones spli() y counter() construye una biblioteca con palabras agrupadas por repeticion.
    Inserta en MongoDB la coleccion de archivos, con sus blibliotecas.
    ........... Mas funcionalidades en contruccion.

#### REQUERIMIENTOS PREVIOS 
||||
|--|---|--|
| Base de datos| [MongoDB](https://docs.mongodb.com/manual/installation/)| Provisionar
| pip | [sudo python3  get-pip.py](https://bootstrap.pypa.io/get-pip.py) | Incluido en el repo
|freeze|[pip install freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/)| instalar previamente
| virtualenv |[sudo pip install virtualenv](https://virtualenv.pypa.io/en/latest/userguide/) | instalar previamente
| pymongo | [Driver MongoDB Python](https://docs.mongodb.com/ecosystem/drivers/pymongo/) | incluido en requirements.txt

#### RECOMENDACIONES PARA CREAR AMBIENTE
```sh
#Crear directorio para lanzar el virtualenv y moverse a el.
mkdir pywords-run && cd pywords-run

#Lanzar el ambiente virtual y activarlo (Podemos desactivarlo con la opcion deactivate)
virtualenv venv && source venv/bin/activate  

#Descargamos los paquetes de la aplicacion al repo wget https://files  .
comandos................................................................

#Instalamos los paquetes al ambiente virtual.
pip install -r requirements.txt
```
#### CONFIGURACION & EJECUCION:
```sh
## config.py

path = "../PATH/"

db_user     ="root"
db_password ="superPower"
db_server   ="127.0.0.1"
dp_port     ="27017"

## No utilizar ROOT como usuario.

```
```sh
## Ejecucion pywords.py


```
