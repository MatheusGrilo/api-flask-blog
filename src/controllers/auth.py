from http import HTTPStatus

from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from src.app import User, db

app = Blueprint("auth", __name__, url_prefix="/auth")


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        return {"error": "Missing username or password"}, HTTPStatus.BAD_REQUEST
    if (
        not (user := User.query.filter_by(username=username).first())
        and not password == user.password
    ):
        return {"error": "Bad username or password"}, HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(identity=user.username)
    return {"access_token": access_token}, HTTPStatus.OK
