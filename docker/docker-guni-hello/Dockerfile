FROM python:3.4.5-slim

# make a local directory
RUN mkdir /app

# set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /app

# copy requirements.txt to /app
ADD requirements.txt .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# copy all the files in this directory to /code
ADD . .

# lisetn to port 80 at runtime
EXPOSE 80

# define our command to be run when launching the container
# -b is a bind command that will route all the ports to route 80
# --workers 4 says how many users can connect
# --reload will reload the webserver when there are changes to the code
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--workers", "4", "--reload"]

