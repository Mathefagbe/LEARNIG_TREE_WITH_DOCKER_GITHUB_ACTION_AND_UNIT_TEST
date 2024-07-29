FROM python:3.8-slim-buster
#pull from the base image on dockerhub
ENV PYTHONUNBUFFERED=1
#create a work directory
WORKDIR /app
#copy requirements.txt
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
#create working directory
COPY . .

#exec form cmd commend
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangotest.wsgi:application"]