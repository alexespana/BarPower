# Material adicional para la elaboración de los hitos
En este documento se encontrará toda la información necesaria para la consecución de los objetivos de la asignatura.

## Documentación correspondiente al objetivo 0
Captura de pantalla donde se visualiza la creación de las [claves pública y privada](img/ssh-keygen.png) y correcta [configuración en github](img/SSHkeys.png)

## Documentación correspondiente al objetivo 1
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