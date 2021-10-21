# Proyecto-IV

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

## ¿Por qué hacer este proyecto? :bulb:
Esta idea ha venido motivada principalmente porque en numerosas ocasiones he visto que bares, cafeterías, pizzerías, etc.., no 
tenían una afluencia adecuada de clientes, no porque sirvieran mala comida sino porque no se preguntaban, ¿qué es lo que a 
nuestros clientes les gusta?, ¿cuáles son los tipos de clientes con los que obtenemos mayor beneficio?. 
Con este proyecto dichos problemas podrían reducirse, aumentando así la productividad y competitividad de estos lugares.

## Historias de usuario :busts_in_silhouette:
Enlaces a las distintas historias de usuario (HU):
* [[HU1]. Anotar clientes y comandas](https://github.com/alexespana/BarPower/issues/9)
* [[HU2]. Predicción de jóvenes](https://github.com/alexespana/BarPower/issues/10)
* [[HU3]. Productos más consumidos en función del cliente](https://github.com/alexespana/BarPower/issues/3)
* [[HU4]. Predicción de ancianos](https://github.com/alexespana/BarPower/issues/4)

## Task runners y gestores de dependencias
Para este proyecto se ha decidido utilizar **invoke** como gestor de tareas y **poetry** como gestor de dependencias. La justificación
de la elección se puede ver reflejada en la documentación adicional al final del documento.

### Invoke
Para la instalación de invoke en Linux debes abrir una terminal y ejecutar el siguiente comando:

    pip install invoke


Si quieres comprobar que se ha instalado correctamente ejecuta en la terminal:

    invoke --version

Comandos obtenidos de la [documentación](https://www.pyinvoke.org/installing.html) de invoke.

### Poetry
Para la instalación de poetry en Linux debes abrir una terminal y ejecutar el siguiente comando:

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Si quieres comprobar que se ha instalado correctamente, abre una nueva terminal y ejecuta:

    poetry --version

Comandos obtenidos de la [documentación](https://python-poetry.org/docs/#installation) de poetry.

### Clase Visits
Esta clase almacenará la información relativa a las visitas que realizan los clientes a lo largo del día en el local. Almacenará los 
tipos de clientes que estén en un momento dado en el bar junto a las horas de llegada, además, almacenará las distintas comandas 
que se realizan por parte de los clientes junto a las horas que se realizan. Esta clase será la encargada de dar toda la lógica de 
negocio de la aplicación, realizando predicciones(usando un teorema probabilístico de Bayes) acerca de la futura presencia de 
determinados tipos de clientes y generando informes sobre los productos más consumidos según tipo de cliente.

Para instalar la clase debes ejecutar:

    invoke install

Para instalar las dependencias necesarias ejecutar:
    
    invoke installdeps


Para comprobar que el resultado de la ejecución es correcto ejecutar:

    invoke test


Para comprobar la sintaxis de esta clase debes ejecutar:
    
    invoke check

## Documentación adicional :books:
[Enlace a documentación](docs/documentacion.md)