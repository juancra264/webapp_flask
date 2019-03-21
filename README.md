Python Flask and mariaDB using Docker Containers
===================================

### Intro
Webapp using docker container one for Ptyhon Flask with MariaDB service.

Project Structure:

```
├── flask
│   ├── crud
│   ├── oldAPP
│   │   └── app
│   │       └── templates
│   └── scripts
│       ├── static
│       │   ├── css
│       │   ├── fonts
│       │   └── js
│       └── templates
├── flasks
│   └── scripts
└── mariaDB
    └── sql

15 directories
```

Once this structure is replicated or cloned with these structure and Docker installed locally, 
you can simply run "docker-compose up" 

### Docker Compose 
Running the compose:
```    
 docker-compose up       (for debug)
 docker-compose up -d    (Dettached from console)
```

Checking the status:  (see what is currently running)
```
 docker-compose ps
```

Stopping compose:
```
 docker-compose stop
```
