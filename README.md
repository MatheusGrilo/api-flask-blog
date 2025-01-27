# API FLASK BLOG

This is a blog API I made with technologies such as Flask and Flask-SQLAlchemy.

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