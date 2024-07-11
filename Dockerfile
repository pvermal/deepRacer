# set base image
FROM quay.io/jupyter/minimal-notebook

RUN pip install --upgrade pip

# set the working directory in the container
WORKDIR /tmp

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .
COPY tracks/ tracks/
COPY racelines/ racelines/

# command to run on container start
# CMD ["python", "./hello_docker.py"]