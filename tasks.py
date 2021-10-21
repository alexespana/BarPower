from invoke import task

@task
def install(context):
    """
    Instala las distintas clases o módulos que tenga el proyecto

    Parameters
    ----------
    context 
        Objeto creado durante el análisis de la línea de comandos
    """
    print("Intalling the program...not yet available")

@task
def installdeps(context):
    """
    Instala las dependencias necesarias para que la aplicación funcione

    Parameters
    ----------
    context 
        Objeto creado durante el análisis de la línea de comandos
    """
    print("Installing the project dependencies")
    context.run("poetry install")

@task
def test(context):
    """
    Comprueba que el resultado del programa sea el correcto
    
    Parameters
    ----------
    context 
        Objeto creado durante el análisis de la línea de comandos
    """
    print("Making tests....not yet available")

@task
def check(context):
    """
    Comprueba la sintaxis de los ficheros python

    Parameters
    ----------
    context 
        Objeto creado durante el análisis de la línea de comandos
    """
    print("Checking syntax of python files in /bar_power")
    context.run("py3compile bar_power/*.py")
