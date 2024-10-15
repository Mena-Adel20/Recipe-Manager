import flask 
from flask import Flask, request, render_template, redirect, url_for, flash,session
import json
from datetime import datetime
import User
import os
from werkzeug.utils import secure_filename

app = Flask("main")
app.secret_key = 'otaku'

# Directory where the uploaded images will be saved
UPLOAD_FOLDER = r"D:\RC\Recipe-Manager\static\uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#**********************************************************************************

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    validation_message = None
    session.pop('email', None)
    
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        # Check if the email exists before adding the user
        error = User.User('users.json', email).add_user(password, username)
        
        # If an error occurs (email already exists), render the signup page with the error message
        if error:
            validation_message = "Email already exists. Please try a different one."
            return render_template('signup.html', validation_message=validation_message)
        
        # Clear the session
        session.clear()
        # If no error, proceed to the login page
        return redirect(url_for('login'))
    
    return render_template('signup.html', validation_message=validation_message)


#**********************************************************************************

@app.route("/", methods=["POST", "GET"])
def login():
    validation_message = None
    if 'email' in session:
        return redirect(url_for('home'))


    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # Read user data from the JSON file
        with open('users.json', 'r') as infile:
            data = json.load(infile)

        # Check if the provided email and password match any user in the data
        for user in data:
            if user['email'] == email and user['pass'] == password:
                # If match is found, set the email in the session and redirect to the home page
                session['email'] = email
                return redirect(url_for('home'))

        # If no match is found, set validation message
        validation_message = "Invalid email or password. Please try again."
        print(validation_message)  # Debugging: See if message is set


    # Pass validation message to the template
    return render_template('login.html', validation_message=validation_message)

#routing to login page
@app.route("/home")
def home():
    # Check  user if not logged in redirect to the login page
    if 'email' not in session:
        return redirect('/')  
    
    return render_template("index.html")
#**********************************************************************************


#routing to all category page
@app.route("/category")
def category():
    # Open and read the categories  from the JSON file
    with open("categories.json", "r") as json_file:
        categories_data = json.load(json_file)
    
    return render_template("categories.html", categories=categories_data["categories"])
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

   
#**********************************************************************************

@app.route("/recipe-details/<id>")
def recipe_details(id):
    # load the recipes  
    with open("recipes.json", "r") as json_file:
        recipes_data = json.load(json_file)
    
        recipe = None
    
    # Iterate recipe in the recipes data
    for r in recipes_data["recipes"]:
        # Check if the ID of the recipe matches the provided ID
        if r["id"] == id:
            recipe = r
            break
    
    
    return render_template("recipeDetails.html", data=recipe)
#**********************************************************************************

def get_next_recipe_id():
    # Load existing recipes and find the next available ID
    with open('recipes.json', 'r') as f:
        data = json.load(f)
        
        if data['recipes']:
            # Find the maximum ID in the existing recipes
            max_id = max(int(recipe['id']) for recipe in data['recipes'])
            return max_id + 1
        else:
            return 1  # Start with ID 1 if no recipes exist  
        

@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    if request.method == 'POST':
        recipe_name = request.form['recipeName']
        category = request.form['category']
        cuisine = request.form['cuisine']
        ingredients_names = request.form.getlist('ingredientName[]')
        ingredients_measurements = request.form.getlist('ingredientMeasurement[]')
        instructions = request.form['instructions']
        time = request.form['time']
        
        # Handle image upload
        photo = request.files['photo']
        photo_filename = None
        if photo:
            photo_filename = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
            photo.save(photo_filename)
            photo_filename = f'../static/uploads/{photo.filename}'

        # Combine ingredients into a list of dictionaries
        ingredients = [{"name": name, "measurement": measurement} for name, measurement in zip(ingredients_names, ingredients_measurements)]

        # Get the next available recipe ID
        new_id = get_next_recipe_id()

        # Create new recipe data
        new_recipe = {
            "id": str(new_id),  # Use the new ID
            "recipe_name": recipe_name,
            "categoryName": category,
            "cuisine": cuisine,
            "ingredients": ingredients,
            "instructions": instructions,
            "time": time,
            "imgLink": photo_filename
        }

        # Append the new recipe to the JSON file
        with open('recipes.json', 'r+') as f:
            data = json.load(f)
            data['recipes'].append(new_recipe)

            # Write updated data back to the JSON file
            f.seek(0)  # Reset the file pointer to the beginning
            json.dump(data, f, indent=4)
            f.flush()  # Ensure it's written to the file system
            f.truncate()  # Remove any leftover content
        email = session.get('email')  # Assuming email is stored in session after login
        if email:

            with open('users.json', 'r+') as user_file:
                user_data = json.load(user_file)
                for user in user_data['users']:
                    if user['email'] == email:
                        user['recipes'].append(str(new_id))
                        user_file.seek(0)  # Reset file pointer
                        json.dump(user_data, user_file, indent=4)
                        user_file.truncate()
                        break

        return render_template('index.html') # Redirect back to the home page

    return render_template('addRecipe.html')


@app.route('/yourrecipes')
def your_recipes():
    email = session.get('email')  # Assuming email is stored in session after login
    if email:
        with open('users.json', 'r') as user_file:
            user_data = json.load(user_file)  # user_data is now a list, not a dict
            user_recipes = []
            
            # Find the user by email in the list of users
            for user in user_data['users']:
                if user['email'] == email:
                    user_recipes = user['recipes']
                    break

        # Fetch recipe details from recipes.json based on user_recipes
        with open('recipes.json', 'r') as recipe_file:
            recipes_data = json.load(recipe_file)
            user_recipe_details = [recipe for recipe in recipes_data['recipes'] if recipe['id'] in user_recipes]

        return render_template('userrecipes.html', recipes=user_recipe_details)
    else:
        flash('Please log in to view your recipes.')
        return redirect(url_for('login'))

    
@app.route('/filter', methods=['GET'])
def filter_recipes():
    # Get the selected filters from query parameters
    selected_cuisines = request.args.getlist('cuisine')
    selected_times = request.args.getlist('time')

    # Load recipes from JSON file
    with open('recipes.json', 'r') as json_file:
        recipes_data = json.load(json_file)

    # If no filters are selected, don't show any recipes
    if not selected_cuisines and not selected_times:
        return render_template('filter.html', recipes=[])

    # Filter recipes based on selected cuisines and times
    filtered_recipes = []
    for recipe in recipes_data['recipes']:
        if (not selected_cuisines or recipe['cuisine'] in selected_cuisines) and \
           (not selected_times or recipe['time'] in selected_times):
            filtered_recipes.append(recipe)

    # Render the 'filter.html' template with the filtered recipes
    return render_template('filter.html', recipes=filtered_recipes)



if __name__ == '__main__':
    app.run(debug=True)
