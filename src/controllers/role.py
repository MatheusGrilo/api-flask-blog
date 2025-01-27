from http import HTTPStatus

from flask import Blueprint, request

from src.app import Role, db

app = Blueprint("role", __name__, url_prefix="/roles")


@app.route("/", methods=["GET", "POST"])
def handle_role():
    if request.method == "POST":
        data = request.json
        role = Role(name=data["name"])
        db.session.add(role)
        db.session.commit()
        return {"message": "Role created!"}, HTTPStatus.CREATED
    else:
        query = db.select(Role)
        roles = db.session.execute(query).scalars()
        return [
            {
                "id": role.id,
                "name": role.name,
            }
            for role in roles
        ], HTTPStatus.OK
