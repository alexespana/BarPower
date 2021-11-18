FROM python:3.8     
LABEL version="0.0.7" maintainer="joaquinalejandroespana@gmail.com"

# Crear usuario que ejecutará el contenedor y el grupo al que pertenece
RUN groupadd -r dockertest && useradd -m --no-log-init -r -g dockertest dockertest

# Declarar el directorio de trabajo (será el de los tests)
WORKDIR /app/test

# Hacer propietario de la carpeta a nuestro usuario
RUN chown dockertest:dockertest /app/test

# Usuario que ejecuta el contenedor
USER dockertest

# Copiar pyproject.toml para poder instalar dependencias más tarde
COPY pyproject.toml /app/test/

# Añadir .local/bin al PATH para incluir instalación de scripts
# como poe por ejemplo
ENV PATH="$PATH:/home/dockertest/.local/bin:${PATH}"

# Instalar herramientas necesarias para el proyecto (poetry y poethepoet)
RUN pip install poetry && \
    pip install poethepoet

# Instalar dependencias declaradas en el archivo pyproject.toml mediante el task runner
RUN poe installdeps

# Pasar los tests
ENTRYPOINT [ "poe", "test" ]
