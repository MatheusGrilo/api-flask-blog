# API FLASK BLOG

This is a blog API I made with technologies such as Flask, Flask-SQLAlchemy, Flask-Migrate.

## Installation

1. Install Poetry:
    ```sh
    pip install poetry
    ```

2. Install dependencies:
    ```sh
    poetry config virtualenvs.in-project true
    poetry install
    ```

## Database Initialization

Run the database initializer:
```sh
poetry run flask --app src.app init-db
```

## Running the Server

- Without debug:
    ```sh
    poetry run flask --app src.app run
    ```

- With debug and hot refresh:
    ```sh
    poetry run flask --app src.app run --debug
    ```

## Extra commands for future devs

- Docker compose with PostgreSQL added in commit [`9e0084d`](https://github.com/MatheusGrilo/api-flask-blog/commit/9e0084df76dba3dc3e4d23ad3ff8cd7fd271e430), SQLite might get errors with migrations because of ForeignKeys 

    ```sh
    # Start PostgreSQL Database (version 17-alpine)
    docker compose up -d
    ```

- Migrations from Flask-Migrate

    ```sh
    # To create a new migration
    poetry run flask --app src.app db migrate-m "Migration name"
    # To upgrade your database
    poetry run flask --app src.app db upgrade
    # To downgrade your database
    poetry run flask --app src.app db downgrade
    ```