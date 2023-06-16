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

## Usuario normal ##

Para ingresar al sistema del usuario principal nos debemos de pocicionar dentro de la carpeta principal de nuestro repositorio. Aquí utilizaremos el siguiente comando para conectarnos:
```
python main_user.py
```
Una vez dentro del sistema se podrá ver el siguiente menú, el cuál le da al usuario un total de 9 acciones para poder interactuar con nuestro programa:


![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/Menu_usuario.png)

#### Consultar Patentes existentes ####

Esta opción nos retorna una lista donde podemos ver todas las patentes que se han registrado en el sistema. Si elegimos esta opción veremos algo como lo siguiente:

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/lista_patentes.png)

### Crear una cuenta ###

En esta opción estaremos creando una cuenta para poder interactuar con Algorand. Esto es importante ya que para la realización de cualquier transacción necesitamos tener algos, y para poder tener algos tenemos que tener una cuenta que nos guarde una cantidad de crédito.

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/creacion_cuenta.png)

Como podemos ver, si damos que sí deseamos crear una cuenta se nos darán dos elementos: **private key mnemonic** la cual es la llave privada de nuestra cuenta y **account address** que corresponde al ID de nuestro usuario dentro de Algorand. Es importante destacar que estos datos los debe de guardar el usuario en algún lugar privado donde los pueda tener a la mano.

### Solicitar Patente ###

Aquí es cuando ya empezamos a interactuar más directamente con Algorand. Esta opción se utiliza para poder obtener una cantidad monetaria que nos permitirá posteriormente crear patentes. Cabe destacar que el administrador es quien se encargará de aprobar nuestras solicitudes de obtención de algos. Veremos en la imagen a continuación que lo primero que hace el sistema es pedirnos el address de la cuenta:

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/peticion_algos_peticion_address.png)

Este address puede ser el generado en el punto dos o el que se tenga guardado dentro de algún archivo, pero es necesario que previamente el usuario ya haya creado una cuenta. Una vez ingresada la cuenta se nos pedirá que indiquemos cuantos algos deseamos solicitar y posterirormente se nos pedirá un número del ticket de pago. Este número puede ser uno aleatorio ya que nuestro sistema aún no genera un número en específico. Si todo sale bien veremos la siguiente imagen:

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/peticion_algos_fin.png)

Si todo sale bien se nos dirá que los administradores revisarán y aprobarán nuestra solicitud a la brevedad. Si queremos ver cuantos algos tenemos podemos utilizar posteriormente la opción de consultar saldo.

### Consultar Saldo ###

Procederemos a explicar la opción número 5 de nuestro sistema ya que está muy relacionada con el punto anterior. Si pedimos consultar el saldo nuevamente veremos un mensaje donde se nos pide nuestro address para saber de que usuario se realizará la petición.

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/consulta_saldo_peticion_address.png)

Una vez que ingresamos la cuenta nos indicará los algos que tenemos disponibles dentro de la cuenta. En la siguiente imagen podemos ver que nuestra cuenta no cuenta con algos disponibles:

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/consulta_saldo.png)

### Solicitar Patente ###

Es importante destacar que para poder pedir una patente se necesita una cuenta que contenga al menos 1 algos, ya que este será el precio a cobrar por la transacción realizada. Si elegimos esta opción debemos de indicar que estamos de acuerdo con que se nos cobre la cantidad de un algo. Posteriormente debemos de ingresar nuestro address y nuestra llave privada, ya que la transacción requiere de la firma del usuario. A continuación se ve la interacción con la termina:

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/crear_patente_peticion_datos.png)

Una vez que nuestros datos sean ingresados aparecerá un forms que debemos de llenar con los datos de nuestra patente. Dependiendo de si somos una persona moral o una física es que formulario se nos pedirá llenar:

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/creacion_patente_tipo_persona.png)

### Consulta tus patentes ###

En esta opción el usuario puede checar las patentes que le han sido aceptadas. 

Posteriormente se deberán de llenar los datos correspondientes.Tras llenar el formulario saldrán los siguientes mensajes. Cabe destacar que toma tiempo la realización de esta petición porque se debe de conectar directamente con _Firebase_ para guardarlas para que el administración pueda revisarlas posteriormente:

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/consulta_patente.png)

Hasta que el administrador de de alta nuestra patente podemos consultarla en el sistema. El sistema nos pedirá que ingresemos nuestro ID. Una vez hecho esto nos indicará cuantas patentes tenemos. El parámetro de _asset-id_ es el id de nuestra patente en Algorand y el parámetro _is_frozen_ nos indica si está en espera para aceptación.

### Consulta más información de la patente ###

En esta opción podremos ver el pdf de cualquier patente que ya haya sida dada de alta en el sistema. Se nos pedirá que ingresemos el nombre 

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/consulta_informacion_cli.png)

Si todo sale bien se abrirá un pdf en un navegador con toda la información que ingresó el usuario en el forms:

![](https://github.com/AlfaroE/Patent-system-with-block-chain/blob/main/images/consulta_informacion_pdf.png)

### Salir ###

Finalmente, si le damos la opción de salir se nos cerrará el sistema.
