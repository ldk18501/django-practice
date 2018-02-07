#!/bin/bash

docker run -d \
  -v /data/mongodb/django:/data/db:rw \
  --name django-mongo mongo:3.4.10

django_mongo_ip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' django-mongo)

docker run -d \
  -e MONGO_URL=$django_mongo_ip \
  --name django-server \
  -p 8000:8000 \
  django-test