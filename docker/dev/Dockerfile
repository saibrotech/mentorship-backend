# official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight to the terminal
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /mentorship-backend

# Set the working directory to /mentorship-backend
WORKDIR /mentorship-backend

# Copy the current directory contents into the container at /mentorship-backend
ADD .. /mentorship-backend/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
