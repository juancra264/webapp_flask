#!/bin/bash
docker run -d -p 3306:3306 \
  --name=mariadb_dckr \
  mariadb
