import flask 
from flask import Flask, request, render_template, redirect, url_for, flash
import json
from datetime import datetime
import User
app = Flask("main")
app.secret_key = 'otaku'  
@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    validation_message = None

    if request.method == 'POST':
        # Retrieve data from the form
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']   
        error = User.User('users.json', email).add_user(password, username)

        if error:
           return render_template('signup.html', validation_message=error) # Return an error message with a 400 status code

        return redirect(url_for('index'))
    return render_template('signup.html', validation_message=validation_message)


#routing to login page
@app.route("/home")
def home():
    return render_template("index.html")

#routing to all category page
@app.route("/category")
def category():
    # Open and read the categories  from the JSON file
    with open("categories.json", "r") as json_file:
        categories_data = json.load(json_file)
    
    return flask.render_template("categories.html", categories=categories_data["categories"])

   
if __name__ == '__main__':
    app.run(debug=True)
