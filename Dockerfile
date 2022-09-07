# pull official base image
FROM python:3.9

# set environment variables
ENV PYTHONUNBUFFERED 1

# set apt-get and install vim
RUN apt-get -y update
RUN apt-get -y install vim

# set work directory
RUN mkdir /thingsflow
ADD . /thingsflow

WORKDIR /thingsflow
ADD requirements.txt /thingsflow

# install dependencies
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt