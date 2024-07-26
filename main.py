from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
import json
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token


app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!


jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Authorization and Authentication
users = []

print("user list", users)
class Register(Resource):
  def post(self):
    print("DAta", request)
    data = request.get_json()
    email = data["email"]   # data.get("email")
    password = data["password"] # data.get("password")

    if email is None or password is None:
      return { "message": "Missing username or password"}, 400

  #  Check if the user exists in the database if not create the instance

    if any(user["email"] == email for user in users):
      return { "message": "Email already exist"}

    users.append({ 'email': email, "password": password})
    return { "message":"Successfuly registered"}, 201


class Login(Resource):
  def post(self):
    data = request.get_json()
    email = data["email"]   # data.get("email")
    password = data["password"] # data.get("password")
    user = next((user for user in users if user['email'] == email and user['password'] == password), None)

    if user is None:
      return { "message": "Invalid credentials"}, 401

    # session["user"] = user

    access_token = create_access_token(identity=email)
    return { "message": "LOgged in" ,  "data": { "user": {"email": email }, "access_token": access_token}}










api.add_resource(Register, "/register")
api.add_resource(Login, "/login")

if __name__ == "__main__":
  app.run(debug=True)
