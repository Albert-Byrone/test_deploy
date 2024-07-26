from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
import json

from flask_restful import Api, Resource


app = Flask(__name__)

api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class HellowWord(Resource):

  def get(self):
    return { "message": "Welcome to the API GET method"}

  def post(self):
    return { "message": "Welcome to the API POST method"}

  def put(self):
    return { "message": "Welcome to the API PUT method"}

  def delete(self):
    return { "message": "Welcome to the API DELETE method"}

api.add_resource(HellowWord, "/")



# # db.init_app(app)
# # url = "https://learn-co-curriculum.github.io/json-site-example/"
@app.route("/users", methods=['GET', 'POST'])
def add_user():
  """Adding a new user
  """
  form = UserForm()


#   users = User.query.all()   # queryset
#   # Serializing
#   # Model(1), Model(2), Model(3),Model(4) dict
#   # Models

#   for user in users:
#     user = {
#       "username":user.username,
#       "email" : user.email
#     }
#     user_list.append(user)

#     return make_response(jsonify(user_list), 200)



#   request = requests.get('https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json')

#   print(request)
#   print(request.text)

#   return json.loads(request.text)



# # Loosly typed
# # http://localhost:3000/api/user/${user_id}
# @app.route("/user/<user_id>")
# def get_user(user_id):
#   """Retrieve a single  user
#   """

# user =User.query.filter(User.id == user_id).first() 1

# user_dict = {
#   "username": user.username,
#   "email": user.email
# }
# return make_response(user_dict, 200)


# {
#   "id": 1,
#   "username": "Albert",
#   "email": "test@gmail.com"
# consum
if __name__ == "__main__":
  app.run()

# RESTFULL APIS
# SOAP APIS

# request ====GET========> https://api.github.com/events ====GET=>   Server
# response <============ https://api.github.com/events <====GET=   Server

# FLASK

# Intro to FLask
#  - WSGI
# - REquest   <====> Response


# SQLAlchemy
#  - CRUD
#  - Database Migrations
#  - Seeding
#  - JSON Response
#  - Serialization

# # RelationSHipn in SQLAlchemy
# -ONe to One
# - One to Mamy
# - Many to MAny

# # Retrieving DAta from API

# - GET Request
# - POstman/Insomia


# # Buiding APIS
# - GET, POST, PATCH, PUT, DELETE

# # RESTFULL API
# - FLask RESTFULL