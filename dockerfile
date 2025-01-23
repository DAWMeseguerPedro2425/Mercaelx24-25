#----UD6.2.h----
#Dockerfile de Mercaelxproy
FROM python:3.10
ENV PYTHONUNBUFFERED 1

# Crea y define el directorio de trabajo dentro del contenedor
RUN mkdir /code
WORKDIR /code

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y \
    postgresql-client
    
# Copia el archivo de requisitos y actualiza pip
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
