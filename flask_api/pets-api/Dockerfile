#
# Pets-API Dockerfile
#
#

# Pull base image
FROM python:3.4.5-slim

# Get some custom packages
RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    gcc \
    python3-dev \
    mongodb 

## make a local directory
RUN mkdir /pets-api

# set 'pets-api' as the working directory from which CMD, RUN, ADD references
WORKDIR /pets-api

# copy all the files in this directory to /code
ADD . .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# listen to port 5000 ar runtime
EXPOSE 5000

# start the app server
CMD python manage.py runserver