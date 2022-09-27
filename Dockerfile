# official Python runtime as a parent image
FROM python:3.10

# The enviroment variable ensures that the python output is set straight to the terminal
ENV PYTHONUNBUFFERED 1

# Exposes port 8000 to the outside world
EXPOSE 8000

# create root directory for our project in the container
RUN mkdir /mentorship-backend

# Set the working directory to /mentorship-backend
WORKDIR /mentorship-backend

# Copy the current directory contents into the container at /mentorship-backend
COPY . /mentorship-backend

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

