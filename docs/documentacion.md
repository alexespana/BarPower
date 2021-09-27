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
de forma fácil y sencilla sus preferencias gastronómicas para poder así disfrutar de un  mejor experiencia.

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
A continuación, voy a explicar un poco más la situación del problema mediante user-jouneys (viaje al cliente).
> "Como Juan Martín (dueño de un bar de la costa de Granada), me gustaría poder saber lo que a la mayoría de mis clientes les gusta consumir, ya sea 
> bebida o comida, además, sería interesante que esto se mostrara de alguna forma gráfica. Muchas veces mis clientes no se muestran satisfechos 
> con el menú y no sé qué servirles, me gustaría tener alguna especie de ayuda a la hora de elegir qué menú viene mejor para un día determinado."

> "Como Ana Rodríguez (mujer de 55 años que suele visitar muchos bares), me gustaría que éstos tuvieran una aplicación donde la carta se pudiese ver con 
> facilidad y con claridad, pudiendo buscar la comida que más me guste mediante el uso de etiquetas, por nombre de comida, los ingredientes que contengan. Para 
> mí sería muy interesante que se pudiese ver el azúcar de cada comida, ya que soy diabética"