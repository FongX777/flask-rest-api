FROM ubuntu:18.04

RUN apt update && \
  apt install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa && \
  apt update -y && \
  apt-get install -y build-essential python3.7 python3.7-dev python3-pip python3.7-venv && \
  RUN python3.7 -m pip install pip --upgrade && \
  python3.7 -m pip install wheel


# Set the working directory to /web
WORKDIR /flask

# Copy the current directory contents into the container at /web 
ADD ./requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

COPY . /flask

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
