FROM python:3.8
WORKDIR /app
#copy the current directory content into the container at /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8000
#Run django development server
CMD ["python","manage.py", "runserver","0.0.0.0:8000"]