# Bar Power

[![CircleCI Tests Status](https://circleci.com/gh/alexespana/barpower.svg?style=svg)](https://circleci.com/gh/alexespana/barpower)
[![readme workflow](https://github.com/alexespana/barpower/actions/workflows/sync.yml/badge.svg)](https://github.com/alexespana/barpower/actions/workflows/sync.yml)
[![docker workflow](https://github.com/alexespana/barpower/actions/workflows/build.yml/badge.svg)](https://github.com/alexespana/barpower/actions/workflows/build.yml)

## Descripción general del proyecto :memo:
La idea de este proyecto será desarrollar un software para ayudar a maximizar la productividad, y por lo tanto la competitividad de los locales
donde se sirva comida, ya sea bares, cafeterías, pizzerías, etc.

A través de las visitas que se vayan realizando al bar, la aplicación irá registrando las comidas, meriendas o cenas que se produzcan, almacenando 
datos como la hora del pedido, el pedido realizado y su precio, con lo que se podrá ofrecer al dueño del bar datos objetivos sobre qué ofrecer y 
mejorar las ganancias del bar.

Se entiende por maximizar las ganancias del bar como vender el mayor número de productos (a ser posible los más caros) en el menor tiempo posible, siempre
por medio de la detección de la aplicación del momento en el que éstas se pueden maximizar atendiendo al tipo de pedidos que se realizan y la clasificación 
que se hace de los clientes.
 
En definitiva, se trata de aumentar el margen de beneficio que los dueños de los bares suelen tener.

---

## ¿Por qué hacer este proyecto? :bulb:
Esta idea ha venido motivada principalmente porque en numerosas ocasiones he visto que bares, cafeterías, pizzerías, etc.., no 
tenían una afluencia adecuada de clientes, no porque sirvieran mala comida sino porque no se preguntaban, ¿qué es lo que a 
nuestros clientes les gusta?, ¿cuáles son los tipos de clientes con los que obtenemos mayor beneficio?. 
Con este proyecto dichos problemas podrían reducirse, aumentando así la productividad y competitividad de estos lugares.

---

## Historias de usuario :busts_in_silhouette:
Enlaces a las distintas historias de usuario (HU):
* [[HU1]. Anotar clientes y comandas](https://github.com/alexespana/BarPower/issues/9)
* [[HU2]. Predicción de jóvenes](https://github.com/alexespana/BarPower/issues/10)
* [[HU3]. Productos más consumidos en función del cliente](https://github.com/alexespana/BarPower/issues/3)
* [[HU4]. Predicción de ancianos](https://github.com/alexespana/BarPower/issues/4)

---

## Task runners y gestores de dependencias
Para este proyecto se ha decidido utilizar **poethepoet** como gestor de tareas y **poetry** como gestor de dependencias. La justificación
de la elección se puede ver reflejada en la documentación adicional al final del documento.

### Poetry
Para la instalación de poetry en Linux debes abrir una terminal y ejecutar el siguiente comando:

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Si quieres comprobar que se ha instalado correctamente, abre una nueva terminal y ejecuta:

    poetry --version

Comandos obtenidos de la [documentación](https://python-poetry.org/docs/#installation) de poetry.

### Poethepoet
Para que poethepoet funcione dentro del entorno de poetry es necesario abrir una terminal y ejecutar el siguiente comando:

    poetry add --dev poethepoet

Para la instalación de poethepoet en tu entorno de python por defecto debes abrir una terminal y ejecutar el siguiente comando:

    pip install poethepoet

Si quieres comprobar que se ha instalado correctamente ejecuta en la terminal:

    poe --version

Comandos obtenidos de la [documentación](https://pypi.org/project/poethepoet/) de poethepoet.


### Clase Visits
Esta clase almacenará la información relativa a las visitas que realizan los clientes a lo largo del día en el local. Almacenará los 
tipos de clientes que estén en un momento dado en el bar junto a las horas de llegada, además, almacenará las distintas comandas 
que se realizan por parte de los clientes junto a las horas que se realizan. Esta clase será la encargada de dar toda la lógica de 
negocio de la aplicación, realizando predicciones(usando un teorema probabilístico de Bayes) acerca de la futura presencia de 
determinados tipos de clientes y generando informes sobre los productos más consumidos según tipo de cliente.

Para instalar la clase debes ejecutar:

    poe install

Para instalar las dependencias necesarias ejecutar:
    
    poe installdeps

Para comprobar que el resultado de la ejecución es correcto ejecutar:

    poe test

Para comprobar la sintaxis de esta clase debes ejecutar:
    
    poe check

Si desea visualizar las tareas disponibles puede ejecutar:

    poe --help

### ¿Por qué usar pytest para testear?
A la hora de la elección del marco de pruebas se planteó la elección de unittest, sin embargo, este marco de prueba tiene una sintaxis más compleja 
y menos legible en comparación con pytest. En el caso de unittest, para testear tendría que crearse una subclase de unittest.TestCase (es decir, que 
heredase de ella), por lo que tendríamos que depender de ello.

El marco de prueba **pytest** tiene una sintaxis más simple, incluye mayor información en el caso de fallo de los tests, y además incluye lo que se 
denominan **fixtures**, que son objetos que si no se crean correctamente, indican que algo va mal, pero si se crean correctamente, se usan como base 
para los tests posteriores. Con respecto a la biblioteca de aserciones se ha decidido usar la de pytest, que comprueba que la expresión pasada como 
argumento es cierta con simplemente hacer **assert <expresion lógica>**

### Fases de test: setup, test y teardown
En este caso, se va a testear la clase Visits. Voy a explicar el procedimiento que seguiremos para realizar los test:
* **Setup**: en esta fase se crean los objetos necesarios para llevar a cabo los test. En nuestro caso, se crea un fixture que será **visits** 
en la función visits(). Si la creación de este objeto se realiza correctamente, será la base para los test siguientes.
* **Tests**: sobre el fixture creado en la fase de setup se llevarán a cabo los tests. Recordar que estos test son independientes de la 
implementación, por lo que debe comprobar comportamiento.
* **Teardown**: en esta fase se eliminan todos los archivos temporales(\__pycache__, .pytest_cache) y se deja al sistema en el estado inicial, para
ello se puede usar la orden **poe clean**.

Como hemos indicado anteriormente, para realizar los test hay que ejecutar:

    poe test

---

## Contenedor para pruebas
Para la creación de nuestro contenedor de pruebas se han seguido una serie de pasos reflejados en la creación del archivo Dockerfile. Como contenedor 
base se ha elegido el oficial de python, en la versión 3.8, ya que es la última versión de python que no está en [modo de corrección de errores](https://devguide.python.org/devcycle/) 
(lo que la hace una versión estable). Lo primero que necesitamos para realizar los test correctamenete dentro de la imagen es tener instaladas las 
herramientas necesarias para ello, por lo que hemos instalado el task runner y el gestor de dependencias (poetthepoet y poetry respectivamente). Además, 
necesitamos que el archivo **pyproject.toml** esté incluido en una carpeta de la imagen, ya que de aquí obtendrá las dependencias (como pytest) que hagan
falta para ejecutar los test. Posteriormente, como acabamos de mencionar, instalamos los módulos/bibliotecas de test a través del task runner. Finalmente, 
ejecutamos los test a través del task runner. 

Al crear la imagen del contenedor he observado que el tamaño de ésta era excesivamente grande (992MB), por lo que he optado por usar una variante contenedor 
base de python más ligera, **python slim**, consiguiendo reducir el tamaño de la imagen significativamente (204MB), haciéndola más ligera.

### ¿Cómo probarlo?
Para probar el correcto funcionamiento del contenedor deberemos descargar este repositorio  y ejecutar dentro de la carpeta raíz del mismo lo siguiente:

    docker run -t -v `pwd`:/app/test alexespana/barpower

En este comando, la opción -t indica cómo Unix/Linux maneja el acceso a la terminal y la opción -v concretamente lo que hace es montar el directorio
local en el que se encuentra a la carpeta /app/test de la imagen, es por esta razón que no ha sido necesario incluir ningún fichero de test ni código fuente 
en la creación de la imagen. La imagen se encuentra almacenada en Dockerhub y puedes acceder a ella [aquí](https://hub.docker.com/r/alexespana/barpower).

---

## Sistema de integración continua 
Hoy en día existe una gran variedad de sistemas de integración continua que pueden usarse para nuestros proyectos, entre los que se pueden encontrar los siguientes:
* Github Actions
* Travis
* Circle CI
* Semaphore CI
* AppVeyor
* Jenkings

Ahora la pregunta sería, ¿cuál puede ser el más recomendado para nuestro proyecto? 

Atendiendo a la facilidad de uso y lo estándar que es el sistema, **Travis** es probablemente el más recomendado de usar, ya que tiene una gran integración con Github, permitiendo 
ver el resultado de la integración continua en la misma página de Github (**checks API**). Sin embargo, dado que para darse de alta exigen tarjeta de crédito (lo cual no todo el 
mundo posee), se ha descartado como opción. Dado que en el objetivo anterior se usó **Github Actions** para configurar la sincronización del README y la actualización del docker, he
decidido descartar usarlos ya que en los tests de la asignatura se comprobará que se haya configurado un sistema de integración continua distinto a Github Actions (que es un falso 
positivo). Siguiendo con la comparativa de los sistemas de CI disponibles, si tuviéramos que elegir entre **Circle CI** y **Semaphore CI**, Circle CI es más aceptado por la comunidad,
ya que tiene una mayor integración con Github que Semaphore CI. Además de ésto se ha comprobado cuál de los dos es el más utilizado actualmente mediante distintos rankings como [este](https://cprimestudios.com/blog/top-cicd-tools-2021-most-complete-guide-33-best-picks-devops) o [este](https://www.slant.co/topics/799/~best-continuous-integration-tools), en el que CircleCI se
encuentra en la 3ª posición y SemaphoreCI en la 16ª y en el que CircleCI está en la 5ª posición y SemaphoreCI en la 10ª, respectivamente. Con respecto al resto de sistemas de CI (AppVeyor y Jenkings), decir que **Jenkings** es el más popular actualmente, sin embargo, no es sólo un sistema de integración continua sino que además es un sistema de entrega/implementación continua, por lo que se ha descartado como opción.

Tras esta comparación, he decidido usar como sistema de integración continua **CircleCI** ya que es sencillo de usar, fácilmente configurable y además tiene una gran integración con Github, permitiendo
incluir fácilmente el [checks API](https://circleci.com/docs/2.0/enable-checks/), de forma que se puedan ver los resultados de la integración continua en Github. Además, nos permite crear y editar el archivo de configuración de la integración continua, llamado **config.yml** desde su interfaz web, corrigiendo errores sintácticos y permitiendo hacer commits del archivo directamente a la rama en la que nos encontremos.

Para más información acerca de la configuración del sistema de integración continua, visite la documentación adicional incluida al final de este archivo.

## Documentación adicional :books:
[Enlace a documentación](docs/documentacion.md)