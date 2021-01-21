# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /web
WORKDIR /web

# Copy the current directory contents into the container at /web 
ADD ./requirements.txt /web/

# Install the dependencies
RUN pip install -r requirements.txt

COPY . /web

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
