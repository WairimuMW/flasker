from flask import Flask, render_template, flash
# flash -> flash messages
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a Flask instance
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = "super secret key that should be hidden" # secret key for csrf token

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