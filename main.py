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

#**********************************************************************************

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

#**********************************************************************************

#routing to login page
@app.route("/home")
def home():
    return render_template("index.html")
#**********************************************************************************


#routing to all category page
@app.route("/category")
def category():
    # Open and read the categories  from the JSON file
    with open("categories.json", "r") as json_file:
        categories_data = json.load(json_file)
    
    return flask.render_template("categories.html", categories=categories_data["categories"])
#**********************************************************************************

#routing to categoty page
@app.route("/category/<category_name>")
def category_name(category_name):

    # Open and read the recipes data from the JSON file
    with open("recipes.json", "r") as json_file:
        recipes_data = json.load(json_file)
    
    filtered_recipes = []
    
    # Iterate over each recipe in the recipes data
    for recipe in recipes_data["recipes"]:
        # Check if the category of the recipe matches the provided category name
        if recipe["categoryName"] == category_name:
            filtered_recipes.append(recipe)
    
    return render_template("categoryDetails.html", recipes=filtered_recipes)

   
if __name__ == '__main__':
    app.run(debug=True)
