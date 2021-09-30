# Material adicional para la elaboración de los hitos
En este documento se encontrará toda la información necesaria para la consecución de los objetivos de la asignatura.

## Documentación correspondiente al objetivo 0
Captura de pantalla donde se visualiza la creación de las [claves pública y privada](img/ssh-keygen.png) y correcta [configuración en github](img/SSHkeys.png)

## Documentación correspondiente al objetivo 1
### Tipos de usuarios  
Esta aplicación tiene dos tipos de usuarios bien diferenciados:
1. Dueño del local: es el usuario que hará un uso más intensivo de la aplicación. El cual quiere saber a través de la aplicación 
qué es lo que sus clientes demandan y que la aplicación le pueda ofrecer datos objetivos como los productos más/menos consumidos según 
el perfil de los clientes que los visitan, generar propuestas sobre qué ofrecer al cliente, etc

2. Cliente: es el usuario que hará uso de la aplicación de forma previa o al acudir al local. Busca que la aplicación recoja 
de forma fácil y sencilla sus preferencias gastronómicas para poder así disfrutar de un  mejor experiencia. En función de los menús que escoja 
tenemos que tener en cuenta tres tipos de clientes:
    1. Con alto poder adquisitivo: usuario que no tiene ningún tipo de problema al pagar las bebidas o platos más caros, siempre está abierto a 
    sugerencias que le pueda ofrecer el dueño del bar, sin importar el precio.
    2. Con un valor adquisitivo medio: este tipo de usuario suele visitar el bar ocasionalmente cuando quiere relajarse tomando unas copas, normalmente 
    suele dejar una cantidad generosa de dinero. La mayoría suele ser gente de joven edad (personas entre los 19-25 años).
    3. Con un bajo poder adquisitivo: usuario que visita el bar muy poco y que cuando lo visita intenta no gastar demasiada cantidad de dinero. Este
    tipo de usuarios suelen repetir en numerosas ocasiones los mismos menús.


Para que los dueños de los locales puedan ver toda esta información acerca del cliente, la aplicación recogerá datos de 
forma implícita. Datos como la hora de llegada al local, la fecha, el producto (entendiéndose como menú, plato, bebida, etc)
seleccionado, etc

### Descripción de los usuarios
1. Juan(dueño de un bar): varón de 30 años, con un nivel de estudios primario (ESO) y habituado al uso de 
aplicaciones. Abrió el bar hace unos meses y está preocupado porque  no va mucha gente por el local. Está buscando 
una solución al problema que haga que la clientela aumente.

2. Ana(cliente): mujer de más de 55 años, con un nivel de estudios superior (grado universitario), poco habituada al uso de aplicaciones móviles, apasionada a la gastronomía 
mediterránea y muy crítica.

### User-journeys
A continuación, voy a explicar un poco más la situación del problema mediante user-jouneys (viaje del cliente).
> "Como Juan Martín (dueño de un bar de la costa de Granada), me gustaría poder saber lo que a la mayoría de mis clientes les gusta consumir, ya sea 
> bebida o comida, además, sería interesante que esto se mostrara de alguna forma gráfica. Muchas veces mis clientes no se muestran satisfechos 
> con el menú y no sé qué servirles, me gustaría tener alguna especie de ayuda a la hora de elegir qué menú viene mejor para un día determinado."

> "Como Ana Rodríguez (mujer de 55 años que suele visitar muchos bares), me gustaría que éstos tuvieran una aplicación donde la carta se pudiese ver con 
> facilidad y con claridad, pudiendo buscar la comida que más me guste mediante el uso de etiquetas, por nombre de comida, los ingredientes que contengan. Para 
> mí sería muy interesante que se pudiese ver el azúcar de cada comida, ya que soy diabética"

> "Como Juan Martín (dueño de un bar de la costa de Granada), me gustaría saber qué clientes de los que están actualmente en el bar son los que más 
> dinero pueden llegar a gastarse en comer. Sería muy interesante tener una estimación de cuál es el mejor momento en el que debo pasar a cambiar 
> el ambiente del bar y ofrecer otros productos como bebidas(copas) y meriendas"


Cuando un cliente llega al bar, éste realizará una búsqueda sobre el plato que desea consumir. Al realizar la selección y encargo del plato/menú, este quedará 
registrado, haciendo que el sistema a partir del precio del producto determine si se trata de un cliente con un valor adquisitivo alto, medio o bajo. En función de esto
y en la hora de realización del pedido se hará una estimación de la edad del cliente.