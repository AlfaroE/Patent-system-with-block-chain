# Bienvenidos al proyecto de Patent-system-with-block-chain #

Para poder utilizar este proyecto se necesita de la instalación de las siguientes bibliotecas de python:
- pip install algosdk
- pip install json
- pip install hash_file
- pip install algorand_utilities
- pip install base64
- pip install subprocess
- pip install random
- pip install hashlib

Este proyecto cuenta con el uso de **algorand** como **API** que nos permite poder crear y enviar algos como moneda de transacción y patentes como activos para nuestra aplicación. Por esto mismo nuestro proyecto utiliza las bilbiotecas de _algosdk_ y _algorand_utilities_ para poder trabajar con algorand y conectarnos a algorand. Igualmente estamos manejando la base de datos de _Firebase_ como base de datos no relacional para tener un sistema que guarde las peticiones del usuario.

Nuestro sistema maneja dos tipos de usuarios: *Usuario normal* y *Usuario administrador*. El usuario normal tiene la capacidad de pedir algos para poder realizar la transacción de solicitar una patente nueva, mientras que el usuario administrador se encarga de aceptar o rechazar las peticiones de los demás usuarios al igual que aceptar o rechazar las peticiones de creación de una patente. Esto último se realiza mediante la conexión a _Firebase_.

A continuación se describirán las acciones posibles que puede realizar cada uno de los usuarios:

### Usuario normal ### 

Para ingresar al sistema del usuario principal nos debemos de pocicionar dentro de la carpeta principal de nuestro repositorio. Aquí utilizaremos el siguiente comando para conectarnos:
```
python main_user.py
```
Una vez dentro del sistema se podrá ver el siguiente menú, el cuál le da al usuario un total de 9 acciones para poder interactuar con nuestro programa:
