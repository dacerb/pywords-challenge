# CHALLENGE: 
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
# ¿Que hace pywords.py ? 
    pywords.py arma una lista de las colecciones ubicadas en la ruta de configuracion cargada en config.py.
    Utilizando las funciones spli() y counter() construye una biblioteca con palabras agrupadas por repeticion.
    Inserta en MongoDB la coleccion de archivos, con sus blibliotecas.
    ........... Mas funcionalidades en contruccion.

#### REQUERIMIENTOS PREVIOS 
||||
|--|---|--|
| Base de datos| [MongoDB](https://docs.mongodb.com/manual/installation/)| Provisionar
| pip | [sudo python3  get-pip.py](https://bootstrap.pypa.io/get-pip.py) | Incluido en el repo
|freeze|[sudo pip install freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/)| instalar previamente
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


## Crear un nuevo ambiente
conda create --name pywords-run
# activar el ambiente
conda activate platzi-mongo
# para desactivar el ambiente
conda deactivate

#Instalamos los paquetes al ambiente virtual y verificamos que esten instalados.
pip install -r requirements.txt && pip freeze
```
##### INSTALACION MONGODB Y CONFIGURACION
```sh
## Instalamos mongoDB en modo no interactivo
sudo apt-get install mongodb -y
## Chequeamos la version
mongod --version
# Configuracion
## Ingresamos a mongodb
mongo

## Ver bases y usuarios
show dbs 
show users

## Creamos base test y configuramos usuario test_usr
use test  # la base de datos no se ve hasta que tenga algun dato cargado
db.createUser( { user: "test_usr", pwd: "SuperTest", roles: [ { role: "readWrite", db: "test" } ] });

## Activamos la opcion de mongo Auth descomentando el archivo de configuracion
sudo  vi /etc/mongodb.conf
# Turn on/off security.  Off is currently the default
#noauth = true
#auth = true

## Descomentamos
auth = true
#### Presionamos ESC  :x!  para guardar y salir utilizando vi editor.

## Regargamos el servicio 
#Usage: /etc/init.d/mongodb {start|stop|force-stop|restart|force-reload|status}
vagrant@ubuntu-bionic:~$ sudo service mongodb restart
## Probamos conectarnos
mongo --port 27017 -u test_usr -p SuperTest --authenticationDatabase test

vagrant@ubuntu-bionic:~$ mongo --port 27017 -u test_usr -p SuperTest --authenticationDatabase test
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/
MongoDB server version: 3.6.3
>

```

#### CONFIGURACION Y EJECUCION:
```sh
## config.py

## Ruta donde se encuentran las colecciones
FILE_PATH = "../PATH/"

## Configuracion para la conexion a MongoDB
MONGO_HOST 	="localhost"
MONGO_PORT 	= 27017
MONGO_DB 	="test"
MONGO_USER	="test_usr"
MONGO_PASS 	="SuperTest"

```
```sh
## Ejecucion pywords.py
python3 pywords.py

##  pygraph.py 
#


```
#### Posibles problemas en VERSION="18.04.2 LTS (Bionic Beaver)"
```sh
## Actualizamos el repositorio en primer lugar.
sudo apt-get update

#Instalacion de get-pip.py
ModuleNotFoundError: No module named 'distutils.util'
Resolvemos instalando el modulo:  [sudo apt install python3-distutils](https://github.com/pypa/get-pip/issues/44)
```
#### RECOMENDACION PARA VIRTUALIZACION DE AMBIENTE:
> Virtualizador [VirtualBOX](https://www.virtualbox.org/wiki/Downloads) 
-	VirtualBox 6.0.14 Oracle VM VirtualBox Extension Pack
-	Guest Additions

> Gestor de entorno virtual [Vagrant](https://www.vagrantup.com/intro/index.html)
-	[Box](https://app.vagrantup.com/ubuntu/boxes/bionic64) | recomendada "ubuntu/bionic64"
-	[Guia de comandos](https://www.vagrantup.com/docs/index.html)
