from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=False)
    email = db.Column(db.String(40),unique=True,nullable=False)
    password = db.Column(db.String(200), primary_key=False,unique=False,nullable=False)
# db.init_app(app)

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=False)
    email = db.Column(db.String(40),unique=True,nullable=False)
    password = db.Column(db.String(200), primary_key=False,unique=False,nullable=False)
# db.init_app(app)

@app.route("/")
def index():
  return "Hello World"

if __name__ == "__main__":
  app.run()




# Relationships
# One to One ==> one record in a table is related with another record from another table
class User(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String,unique=False)
  profile =db.relationship('Profile', backref="user")


class Profile(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  bio = db.Column(db.String)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True)
# profile.user
# One to Many ==> one record in a table is related with many records from another table
class Author(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String,unique=False)
  books =db.relationship('Book', backref="user")


class Book(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  bio = db.Column(db.String)
  author_id = db.Column(db.Integer, db.ForeignKey("author.id"), unique=True)

# Many to Many ==> many records in a table are related with many records from another table,
# defined by having an association table

# Student
# Coursers

association_table = db.Table("association",
  db.Column('student_id', db.Integer, db.ForeignKey("student.id")),
  db.Column('course_id', db.Integer, db.ForeignKey("course.id"))
)


class Student(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String,unique=False)
  courses =db.relationship('Course', backref="user")


class Course(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String)


# Primary Key Contraints
# class User(db.Model):
#   id = db.Column(db.Integer,primary_key=True)

# Unique Contraints
# class User(db.Model):
#   id = db.Column(db.Integer,primary_key=True)
#   name = db.Column(db.String,unique=True)

# Foreign Key Contraints
# class User(db.Model):
#   id = db.Column(db.Integer,primary_key=True)
#   name = db.Column(db.String,unique=True)
#   post_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True)


# Default Contraints
# class User(db.Model):
#   id = db.Column(db.Integer,primary_key=True)
#   name = db.Column(db.String,unique=True)
#   gender = db.Column(db.String,default="Male")


# Custom class Model validation
class User(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String,unique=True)
  age =  db.Column(db.Integer, nullable=False)

  # validation
# between 4 and 25 chars
  def validate(self):
    if len(self.name) < 4 orlen(self.name) > 25:
      raise valueError("Name must be between 4 and 25 characters")

    if self.age < 18:
      raise valueError("Must be 18 and above")


