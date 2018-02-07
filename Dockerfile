FROM python:3.6.4-alpine

RUN mkdir -p /code/myserver

WORKDIR /code

COPY myserver /code/myserver/

COPY requirements.txt /code

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD python myserver/manage.py runserver 0.0.0.0:8000