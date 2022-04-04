#import image
FROM python:3.7-alpine

#install dependencies
RUN pip install Django==2.1.15

#make app directory
RUN mkdir /app

#use app directory
WORKDIR /app

#copy aplication files to directory
COPY ./mysite /app

#run django app 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]