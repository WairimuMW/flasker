from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__, template_folder='templates')

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


# 1. Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500