# Use an official Python runtime as a parent image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install python
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN apt-get install -y git
RUN pip install gitpython
RUN pip install PyGithub

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ARG GIT_COMMIT
ENV GIT_COMMIT ${GIT_COMMIT}
ENV CONTAINER_TIMEZONE TZ=Europe/Kiev


# Run app.py when the container launches
CMD ["python", "web_pyth_final.py"]
