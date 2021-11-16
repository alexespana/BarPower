FROM python:3.8     
LABEL version="0.0.7" maintainer="joaquinalejandroespana@gmail.com"

# Declarar el directorio de trabajo (será el de los tests)
WORKDIR /app/test

# Copiar pyproject.toml para poder instalar dependencias más tarde
COPY pyproject.toml /app/test/

# Instalar herramientas necesarias para el proyecto (poetry y poethepoet)
RUN pip install poetry && \
    pip install poethepoet

# Instalar dependencias declaradas en el archivo pyproject.toml mediante el task runner
RUN poe installdeps

# Pasar los tests
ENTRYPOINT [ "poe", "test" ]
