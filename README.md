# todoapp-flask

To init a PostgreSQL database for the project:

```docker run -d --name postgresql -e 'DB_USER=admin' -e 'DB_PASS=admin' -e 'DB_NAME=todo' -p 5432:5432 sameersbn/postgresql:9.4-4```

To run a container for the application:

```docker run -d -p 5000:5000 --link postgresql:postgres --name todo todoapp```
