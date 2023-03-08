from flask import Flask, render_template, flash
# flash -> flash messages
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create a Flask instance
app = Flask(__name__, template_folder='templates')

# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# secret key for csrf token
app.config['SECRET_KEY'] = "super secret key that should be hidden"

# initialize the database
db = SQLAlchemy(app)

# def create_app():
#     app = Flask(__name__)

#     with app.app_context():
#         db()

#     return app

# create model -> what you want to store in the db
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(200), nullable=False)
    email =  db.Column(db.String(120), nullable=False, unique=True)
    date_added =  db.Column(db.DateTime, default=datetime.utcnow)
    
    # create a string
    def __repr__(self):
        return '<Name %r>' % self.name

# User form
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")    

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    # Fields
        # BooleanField
        # DateField
        # DateTimeField
        # DecimalField
        # FileField
        # HiddenField
        # MultipleField
        # FieldList
        # FloatField
        # FormField
        # IntegerField
        # PasswordField
        # RadioField
        # SelectField
        # SelectMultipleField
        # SubmitField
        # StringField
        # TextAreaField
    
    # Validators
        # DataRequired
        # Email
        # EqualTo
        # InputRequired
        # IPAddress
        # Length
        # MacAddress
        # NumberRange
        # Optional
        # Regexp
        # URL
        # UUID
        # AnyOf
        # NoneOf

# Create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

# SOME jinja FILTERS!!!
# safe -> for injecting html without jinja stripping it out
# capitalize -> capitalizes the first letter
# lower -> converts to lowercase
# upper -> converts to uppercase
# title -> capitalizes every 1st letter of every word
# trim -> removes trailing spaces from the end
# striptags -> strips any html tags



def index():
    first_name = "Mary"
    blah = "This is <strong>Bold</strong> Text"
    blah2 = "a new title"
    
    pizza = ["Pepperoni", "Cheese", "Mushrooms", 42]
    return render_template("index.html", 
                           first_name=first_name,
                           blah=blah,
                           blah2=blah2,
                           pizza=pizza
                           )

# localhost:5000/user/Wairimu ... -> allows us to pass a name
@app.route('/user/<name>')

# without template
# def user(name):
#     return "<h1>Hello {}!!!</h1>".format(name)

# using a template
def user(name):
    return render_template("user.html", user_name=name)


# Create custom error pages

# 1. Invalid URL
@app.errorhandler(404) 
def page_not_found(e):
    return render_template("404.html"), 404


# 2. Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # validate the form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!") # our flash message
    return render_template("name.html",
                           name = name,
                           form = form)


# add user page
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    
    # validate form
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User added successfully!")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", 
                           name=name, 
                           form=form,
                           our_users=our_users)