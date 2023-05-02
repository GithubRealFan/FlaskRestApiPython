# Flask Rest API

![image](https://user-images.githubusercontent.com/121934188/235756123-e7a528cd-8fd9-4819-b1d0-ae7de0e11af8.png)

# Design a RESTful API with Python and Flask

In recent years REST (REpresentational State Transfer) has emerged as the standard architectural design for web services and web APIs.

In this article I'm going to show you how easy it is to create a RESTful web service using Python and the Flask microframework.

Code available on my Repo

## What is REST?
It’s an architectural style for designing standards between computers, making it easier for systems to communicate with each other. In simpler terms, REST is a set of rules developers follow when they create APIs.

A system is called RESTful when it adheres to these constraints.RESTful APIs almost always rely on HTTP. When we are working with APIs, a client will send an HTTP request, and the server will respond with the HTTP response.

## Installation
To set up a Python server, you need to install Python, I would suggest any version above 3.7 as of the year 2019.

- Download the latest Python version from the python.org

- Once installed, open up your terminal/cmd and install flask.

$ pip install Flask
// or
$ py -m pip install Flask

- Once flask is installed, we’ll need to set up a virtual environment to run our application.

## Setting up a Virtual Environment.

- We’ll start by creating a folder and adding a venv folder within.
$ mkdir sandbox
$ cd sandbox
$ py -m venv venv
- To activate the environment, navigate to venv/bin/activate on Linux.
- On windows, use cmd and navigate to venv/Scripts/activate
- Navigate back to sandbox which is root and create a file app.py .

## Create a minimal Flask application.
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/greet')
def say_hello():
  return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True)
Here, we import Flask class and create an instance of it. To create an instance, we’d have to give it a name and using (__name__) ensures that it can be started as an application or imported as a module.

We the use the route() decorator to let our flask app know which
URL should trigger the corresponding method. The function then simply returns a string message using different URLs in the example.

 It’s important to note that by default, @app.route has a GET method. 
 If we want to use any other HTTP verbs, we have to specify them by passing 
 them via the methods parameter as a list.
To run the appliaction, we have to complete a few things first. So, set the environment to development and tell your terminal the application to work with by exporting the FLASK_APP environment variable in Linux.

$ export FLASK_ENV=development
$ export FLASK_APP=app.py

and windows.

$ set FLASK_ENV=development
$ set FLASK_APP=app.py

Run using.

$ flask run
// or
$ py -m flask run
* Running on http://127.0.0.1:5000

By default, the port is 5000 .

You’ve successfully created your first Python server using Flask. It’s quite basic and returns string responses, let’s spice things up a little by learning some more things we can do.

## Routing.
Routes are considered to be endpoints, you can create different routes for your endpoints that use different methods.

We use the route() decorator to bind a function to a URL. Here’s a number of routes with details in the comments.
@app.route('/')
def index():
 return 'Index Page'

@app.route('/hello')
def hello():
 return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/user/<username>')
def show_user(username):
 #returns the username
 return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
 #returns the post, the post_id should be an int
 return str(post_id)
By default, a route only answers to GET requests. You’ll have to import request from flask to identify the type of method used.
from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    #check user details from db
    login_user()
  elif request.method == 'GET':
    #serve login page
    serve_login_page()
## Rendering Templates.
When using express.js, Pug is the default template engine. Well, in Flask we use Jinja2.
Flask configures Jinja2 automatically when installing, and to render templates all you would need is to import render_template from flask and variables you would want to pass to the template engine as keyword arguments.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def hello(name=None):
 #name=None ensures the code runs even when no name is provided
 return render_template('user-profile.html', name=name)
You can learn more about Jinja2 here.

Accessing Request Data.
You might want to pass data via the more secure POST method as opposed to exposing it via the URL. To access form data (transmitted via POST or PUT methods), you can use the form attribute.
from flask import Flask, request

app = Flask(__name__)

@app.route('/user', methods=['GET','POST'])
def get_user():
 username = request.form['username']
 password = request.form['password']
 #login(arg,arg) is a function that tries to log in and returns true or false
 status = login(username, password)
 return status
If the keys username or password does not exist, then a special KeyError is raised. You can catch it like any other error but if you don’t do that, a HTTP 400 (Bad Request) error page is shown. To access parameters submitted in the URL ( ?key=value ) you can use the args attribute.

searchkeyword = request.args.get('key': '')

It’s recommended to catch KeyError when using URL parameters as some users can
change the URL which may return a Bad Request error page.

## File Uploads.
Python is a very simple language, it gets even simpler using Flask to upload images, files or videos. Flask allows you to upload files from a form object, just make sure you set enctype="multipart/form-data" attribute on your form.

While uploaded files are temporalily stored in memory or at a temporary location in the file system, you can use the save() method to store the file in the server file system.

When you create a server, it’s not recommended you store files on the server, you should store files to a service like AWS Storage, Firebase (by Google), Azure (Microsoft),
Dropbox and others and only keep the url to these files stored in a separate database as strings, maybe even in the server.
However, here’s how you can save files on the server just incase you just want to.
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        static_file = request.files['the_file']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
        static_file.save('/var/www/uploads/profilephoto.png')
You can access your file using the hostname of your server plus the file directory after saving to the file system.i.e

https://myapp.com/var/www/uploads/profilephoto.png
