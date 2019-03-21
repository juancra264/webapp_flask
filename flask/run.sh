#!/bin/bash
sh stop.sh
docker run -d -p 80:5000  \
    --volume=/home/jcramirez/docker/webapp_flask/flask/scripts:/app \
    --name=flask_dckr flask_dckr:latest
