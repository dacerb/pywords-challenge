# CHALLENGE:

Desarrolle un programa que le permita obtener los siguientes valores sobre la colección de documentos adjunta:

- Cantidad de palabras diferentes en la colección
- Cantidad de documentos X
- Determinar cuál es el documento con más palabras X

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

Empleando la librería que considere adecuada, grafique distribución de las diez palabras con mayor frecuencia. 

# ¿Que hace pywords.py ?

  pywords.py arma una lista de los documentos de la coleccion ubicada en la ruta de configuracion cargada en config.py.
  Construye una biblioteca con palabras agrupadas por repeticion. Las inserta en MongoDB, y devuelve el resultado:

  - Cantidad de palabras diferentes en la colección
  - Cantidad de documentos
  - Determinar cuál es el documento con más palabras
  - Grafique las diez palabras con mayor frecuencia

#### REQUERIMIENTOS PREVIOS

||||
|--|---|--|
| Base de datos| [MongoDB](https://docs.mongodb.com/manual/installation/)| Provisionar
| pip | [sudo python3  get-pip.py](https://bootstrap.pypa.io/get-pip.py) | Incluido en el repo
|freeze|[sudo pip install freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/)| instalar previamente
| virtualenv |[sudo pip install virtualenv](https://virtualenv.pypa.io/en/latest/userguide/) | instalar previamente
| python3 | instalación de metodos | incluido en requirements.txt

#### RECOMENDACIONES PARA CREAR AMBIENTE

```sh
#Crear directorio para lanzar el virtualenv y moverse a el.
- mkdir pywords-run && cd pywords-run

- Clonamos el repositorio de Pywords

- Instalamos pip sudo python3  get-pip.py

- Instalamos virtualenv sudo pip install virtualenv

# Activamos el ambiente virtual
- virtualenv venv && source venv/bin/activate  

#Instalamos los paquetes en el ambiente virtual y verificamos que esten instalados.
pip install -r requirements.txt && pip freeze
```

##### INSTALACION MONGODB EN LINUX CONFIGURACION

```sh

## Instalamos mongoDB en modo no interactivo
sudo apt-get install mongodb -y

## Ingresamos a mongodb
mongo

## Ver bases y usuarios
show dbs
show users

## Creamos base test y configuramos usuario test_usr
use test        # la base de datos no se ve hasta que tenga algun dato cargado
db.createUser( { user: "test_usr", pwd: "SuperTest", roles: [ { role: "readWrite", db: "test" } ] });

## Probamos conectarnos
mongo --port 27017 -u test_usr -p SuperTest --authenticationDatabase test

vagrant@ubuntu-bionic:~$ mongo --port 27017 -u test_usr -p SuperTest --authenticationDatabase test
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/
MongoDB server version: 3.6.3
>

```

#### CONFIGURACION DE PYWORDS PARA CONECTAR A MONGO:

```sh
## config.py

## Ruta donde se encuentran las colecciones
FILE_PATH = "../PATH/"

## Configuracion para la conexion a MongoDB
MONGO_HOST 	="localhost"
MONGO_PORT 	= 27017
MONGO_DB 	  ="test"
MONGO_USER	="test_usr"
MONGO_PASS 	="SuperTest"

```

```sh
## Ejecucion pywords.py

# Activamos el ambiente virtual
# Revisamos que esten instalados los paquetes necesarios pip freeze
# Ejecutamos
python3 pywords.py
# Al final de ejecutar tenemos como resultado
# los datos en la base de mongo
# y una ventana grafica con los valores de las operaciones

## Actualizamos el repositorio en primer lugar.
sudo apt-get update