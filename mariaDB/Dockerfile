FROM mariadb:latest
MAINTAINER juancra264 "juancra264@hotmail.com"
ADD ./sql /docker-entrypoint-initdb.d
### For stand alone container test......
#ENV MYSQL_ROOT_PASSWORD prueba.2019
#ENV MYSQL_DATABASE crud
#ENV MYSQL_USER dbuser
#ENV MYSQL_PASSWORD prueba.2019
#RUN apt-get update
#RUN apt-get update && apt-get -y install vim
#EXPOSE 3306
#CMD ["mysqld"]:
