# Material adicional para la elaboración de los hitos
En este documento se encontrará toda la información necesaria para la consecución de los objetivos de la asignatura.

## Objetivo 0
Captura de pantalla donde se visualiza la creación de las [claves pública y privada](img/ssh-keygen.png) y correcta [configuración en github](img/SSHkeys.png)

---

## Objetivo 1
### Tipos de usuarios que usarán la aplicación
Esta aplicación tiene dos tipos de usuarios bien diferenciados:
1. Dueño del bar: es el usuario que hará un uso más intensivo de la aplicación. El cual quiere saber a través de la aplicación cuándo sus 
clientes están demandando un mayor consumo de productos.

2. Camareros: son usuarios que harán un uso de la aplicación en su jornada laboral, conforme los clientes vayan llegando al bar éste irá apuntando el tipo de cliente que llega según una clasificación de grupos de clientes, siempre bajo su propia suposición.

### Clasificación de los clientes
Son las personas que acuden al bar. Atendiendo el criterio propio del camarero que los atiende, los clientes podrán clasificarse en 
cuatro grupos atendiendo el siguiente criterio:
* Niño: persona de entre 5 y 15 años
* Jóven: persona de entre 16 y 30 años
* Adulto: persona de entre 31 y 65 años
* Anciano: persona mayor de 65 años

### User-journey
A continuación, voy a explicar más detalladamente en qué consiste el problema a resolver y cómo se puede llevar a cabo.
El objetivo principal de la aplicación es ofrecer al dueño del bar o a los camareros indicaciones de qué tipo de clientes están realizando 
un mayor consumo de productos(menús, platos, bebidas, postres, etc) en determinados tramos horarios del día y en tiempo real obviamente.

Cuando un usuario o grupo de usuarios llega al bar, el camarero que los atiende anotará según su criterio, qué tipo de usuario/usuarios (de acuerdo a los tipos 
especificados anteriormente) son, de esta forma se almacenará el tipo de usuarios y la hora a la que realizan la visita. Además, cuando un usuario realice un pedido, el 
camarero anotará dicho pedido, quedando por lo tanto almacenado el pedido y la hora a la que se realiza. 

De este modo, por un lado tendríamos los tipos de clientes que visitan el bar con sus respectivas horas de visita y por otro, los pedidos realizados y las horas 
a las que estos se producen. Se pretende hacer predicciones sobre qué momentos se está realizando un mayor consumo de productos y qué tipo de clientes es más 
probable que lo este realizando.

### Descripción de los usuarios
1. Juan(dueño de un bar): varón de 30 años, con un nivel de estudios primario (ESO) y habituado al uso de 
aplicaciones. Abrió el bar hace unos meses y está preocupado porque al haber gran cantidad de clientela no puede controlar bien en qué momento 
es necesario cambiar el ambiente del bar o servir platos más apropiados según los clientes que tiene en el bar.

2. Ana (camarera): chica de 20 años, ha empezado a trabajar hace pocos meses y no tiene muy claro las preferencias que tienen los clientes, (sobre todo adultos y ancianos) 
a la hora de hacerles una petición de lo que pueden consumir. Le gustaría que la aplicación con los datos actuales del bar le hiciera una sugerencia (predicción) de qué es más 
probable que se consuma en función del cliente que sea.

---

## Objetivo 3
### Elección del task runner y del gestor de dependencias 
Makefile es uno de los gestores de tareas más simples y conocidos por ser una herramienta genérica, igualmente, python tiene su task runner específico **invoke** 
que proporciona una API limpia y fácil de entender (de alto nivel) para organizar tareas, sin embargo, este último daba problemas con poetry, por lo que finalmente he optado 
por usar **poethepoet** 

La principal razón de **poetry** como gestor de dependencias es que tiene una [documentación](https://python-poetry.org/) muy buena y clara, tiene una fácil configuración del archivo principal (**pyproject.toml**) y permite añadir las dependencias automáticamente con simplemente incluir el comando poetry add \<dependencia>.

Con respecto a la herramienta para comprobar la sintaxis de los archivos python, se planteó utilizar **pylint** ya que tiene muchas funcionalidades como comprobador de sintaxis, comprobador de estilo de acuerdo a PEP8 y demás, sin embargo, a la hora de ejecutarlo desde invoke daba problemas ya que poetry tiene su propio entorno e instalaba pylint en su entorno, por lo que tendríamos que decirle a invoke que ejecutase pylint desde el entorno de poetry. Dado que el único objetivo de la orden check es comprobar si los archivos compilan, se ha optado por usar la opción más sencilla, **py3compile**.

Para solucionar este último inconveniente que menciono de invoke, he decidido cambiar el task runner elegido por **poethepoet**, un gestor de tareas que funciona bien con poetry. En este caso cuando 
ejecutamos desde nuestra terminal poethepoet, éste se ejecuta desde el entorno de poetry, además, poetry nos permite definir sus tareas desde el archivo pyproject.toml, lo que hace que definir tasks
de poethepoet sea limpio y sencillo.

---

## Objetivo 5 
### Elección del contenedor base
Nuestro contenedor base debe cumplir con una serie de requisitos necesarios para nuestra imagen:
* Que sea ligero
* Que no genere problemas de paquetes no instalados

Para la elección del contenedor base se planteó al principio elegir el propio de una distribución de ubuntu, sin embargo, la imagen de ubuntu incluye todas las herramientas del sistema, herramientas que no serían necesarias para pasar los tests, por lo que dicha opción se descartó. Únicamente lo que nos hace falta es tener python en la imagen, ahora tocaría preguntarse, ¿con qué versión? Tras investigar en la página oficial de [python](https://www.python.org/downloads/) y comprobar qué quiere decir el **maintenance status** en la [siguiente página](https://devguide.python.org/devcycle/), se ha decidido elegir la versión 3.8, ya que es la última versión de python que no está en modo de corrección de errores (lo que la hace una versión estable).

Tras crear nuestra primera imagen con el contenedor base python:3.8 observé que no cumplía con uno de nuestros requisitos básicos, ser ligero, ya que ocupaba 992MB, el cuál es un tamaño excesivamente grande, además del tiempo que se necesitaba para descargar o actualizar la imagen en Dockerhub. Tras esto se probó entre distintas versiones de contenedores base de python como pueden ser **alpine** y **slim**. El contenedor base python:3.8-alpine podría ser una buena opción ya que tiene un tamaño muy reducido en comparación con la imagen base del lenguaje, sin embargo, en imágenes dónde se use python, puede hacer que las imágenes sean lentas y grandes ([Enlace de interés](https://pythonspeed.com/articles/alpine-docker-python/)). El contenedor base python:3.8-slim, al igual que alpine, tiene un tamaño muy reducido, no contiene los paquetes comunes contenidos en la imagen base por defecto y además sólo contiene los páquetes mínimos para poder correr python. Tras crear nuestra imagen usando este contenedor base se pudo comprobar que cumplía nuestros dos requisitos, ser de tamaño reducido (hemos pasado de 992MB usando python:3.8 a 204MB usando python:3.8-slim) y no generar problemas de paquetes no instalados, cosa que ocurría con alpine.

Esta elección se ha llevado a cabo usando siempre como guía las [mejores prácticas](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) de docker.

---

## Objetivo 6
### Configuración del sistema de integración continua
#### Ejecutar tests automáticamente
El principal objetivo de añadir un sistema de integración continua a nuestro proyecto es asegurar que el código pasa todos los tests antes de ser desplegado o simplemente (como en este caso) incorporado a la rama principal, por lo que configuraremos nuestro repositorio para que se pasen los tests automáticamente.

Dado que el sistema de CI elegido es CircleCI, se precisa de un archivo llamado **config.yml** para su configuración, que se encuentra en la carpeta **.circleci**. A continuación voy a proceder a explicar su contenido:
* **version: 2.1**: es la versión de CircleCI incluida por defecto por el generador automático de configuraciones de CircleCI.
* Ahora pasamos a definir los jobs necesarios para pasar los tests, en este caso solo será necesario uno, al que llamamos **ejecutar-tests**
    * **executor**: éste define la tecnología o entorno subyacente donde se va a ejecutar una tarea. Éstos pueden ser de cuatro tipos: ***docker, machine, macos o windows***.
    Dado que queremos aprovechar el contenedor de Docker creado en el objetivo anterior (que únicamente contiene los módulos/bibliotecas necesarios para pasar los tests) necesitaremos 
    que nuestro entorno de ejecución (donde se ejecute la tarea) tenga acceso completo al proceso de docker, por esta razón el executor es **machine** (máquina virtual de linux).
        * **image: ubuntu-2004:202111-01**: en principio la imagen elegida para ejecutar docker no es especialmente relevante en este caso, ya que únicamente ejecutaría el contenedor
        que ya tenemos para pasar los tests. En este caso se ha elegido la última imagen disponible, que tiene las siguientes especificaciones: Ubuntu 20.04, Docker v20.10.11 y
         Docker Compose v1.29.2.
    * **Steps**: son los pasos que se van a llevar a cabo en la tarea.
        * checkout: comprueba el código fuente del repositorio ([more info](https://circleci.com/docs/2.0/configuration-reference/#checkout)).
        * command: docker run -t -v `pwd`:/app/test alexespana/barpower: ejecuta los tests sobre el repositorio. El hecho de usar un contenedor para pasar los tests hace que éstos se ejecuten
        de una forma más rápida y eficiente.
* Finalmente, indicamos los jobs que queremos ejecutar, en este caso **ejecutar-tests**.

CircleCI por defecto pasará los tests automáticamente cada vez que se haga push al repositorio.

#### Versiones del lenguaje con las que funciona
En esta configuración se ha decidido testear la aplicación con distintas versiones del lenguaje python. Comprobando las [dependencias](https://github.com/alexespana/barpower/blob/Objetivo-6/pyproject.toml) requeridas por nuestra aplicación, vemos que las versiones soportadas serían las iguales o superiores a la versión 3.8 de python, por lo que se testeará la aplicación con la versión más antigua soportada por la configuración de poetry, **versión 3.8** (última versión estable) y todas las versiones posteriores, las **versiones 3.9** y **3.10**. Entre los detalles más importantes de la configuración tenemos:

* **strategy**: esta palabra clave indica que queremos crear una matriz de compilaciones.
    * **matrix**: será nuestra matriz de compilaciones, esta matriz de compilaciones ejecutará el job varias veces (tres veces en concreto) utilizando distintas versiones de python, que están especificadas en **python-version**.
* Usamos una github action ya definida en el [marketplace](https://github.com/marketplace/actions/setup-python) para establecer la versión de python a usar (3.8, 3.9 y 3.10).
* Finalmente, testeamos la aplicación sobre los fuentes del repositorio.

Este job que hemos definido se ejecutará tantas veces como distintas versiones del lenguaje hayamos indicado (en este caso 4) y además, cada uno de estos flujos se ejecutará de forma paralela.

---

## Objetivo 7
### Nuevo nivel de abstracción
Teniendo en cuenta uno de los principios SOLID, la O viene a decir que el código que se escribió debe estar preparado de forma que se prevea su cambio en el futuro, Open/Close, abierto a extensión, **cerrado a modificación**, por lo que las clases que ya tenemos no debemos modificarlas.

Por esta razón, deberemos de realizar el logging en un nivel superior de abstracción. Para ello se ha decidido crear la clase Handler, que realiza el logging de la aplicación. En ella hemos importado el contenido del archivo logger.py. En este archivo se leen las variables de configuración de la aplicación por medio de un objeto Config que contiene la configuración de la aplicación. En dicho archivo se ha realizado lo siguiente:
1. Aparte de leer el directorio de logs y el archivo de logs desde la configuración, también se ha creado de forma recursiva el directorio de logs especificado en la configuración, ya que este directorio podría no estar, realizándose de forma incorrecta el logging por lo tanto.
    ```shell
    if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY, exist_ok=True)
    ```
2. Finalmente se ha realizado la configuración del logger, teniendo en cuenta que:
    ```shell
    logging.basicConfig(filename=LOG_DIRECTORY + LOG_FILE, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s' )
    ```
    * filename: indica el fichero de logs
    * level: indica el umbral a partir del cual se registran los logs, en este caso DEBUG, el más bajo.
    * format: indica el formato de los mensajes de log. 
