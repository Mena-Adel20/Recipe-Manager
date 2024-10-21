from flask import Flask, request, render_template, redirect, url_for, flash,session
from database import Database
from recipe_manager import RecipeManager
from user_manager import UserManager
import os

app = Flask("main")
app.secret_key = 'otaku'

# Directory where the uploaded images will be saved
UPLOAD_FOLDER = r".\static\uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = Database()
recipe_manager = RecipeManager(db)
user_manager = UserManager(db)

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
        error = user_manager.add_user(email, password, username)
        
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

@app.route("/login", methods=["POST", "GET"])
def login():
    validation_message = None
    if 'email' in session:
        return redirect(url_for('home'))

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # Read user data from the JSON file
        data = db.load_json('users.json')
        # Check if the provided email and password match any user in the data
        for user in data['users']:
            if user['email'] == email and user['pass'] == password:
                # Store the email and name in the session
                session['email'] = email
              
                return redirect(url_for('home'))

        validation_message = "Invalid email or password. Please try again."

    return render_template('login.html', validation_message=validation_message)

#**********************************************************************************
@app.route("/")
def home():
    # # Check if user is not logged in, redirect to the login page
    # if 'email' not in session:
    #     return redirect('/')

    categories_data = db.load_json("categories.json")
    return render_template("index.html", categories=categories_data["categories"])

#**********************************************************************************

#routing to categoty page
@app.route("/<category_name>")
def category_name(category_name):

    recipes_data = db.load_json("recipes.json")
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
    recipe = recipe_manager.get_recipe(id)
    return render_template("recipeDetails.html", data=recipe)
#**********************************************************************************      

@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    if 'email' not in session:
        flash('Please log in to view your recipes.')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        photo = request.files['photo']
        photo_filename = None
        if photo:
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo.filename))
            photo_filename = f'../static/uploads/{photo.filename}'

        recipe_data = {
            'recipe_name': request.form['recipeName'],
            'category': request.form['category'],
            'cuisine': request.form['cuisine'],
            'ingredients': [{"name": n, "measurement": m} 
                          for n, m in zip(request.form.getlist('ingredientName[]'),
                                        request.form.getlist('ingredientMeasurement[]'))],
            'instructions': request.form['instructions'],
            'time': request.form['time']
        }
        recipe_id = request.form.get('id')  # Get the ID from the form

        recipe_manager.add_recipe(recipe_data, photo_filename,recipe_id)



        if 'email' in session:
            user_manager.add_recipe_to_user(session['email'], recipe_id)

        return redirect(url_for('home'))

    return render_template('addRecipe.html')

#**********************************************************************************

@app.route('/yourrecipes')
def your_recipes():
    if 'email' not in session:
        flash('Please log in to view your recipes.')
        return redirect(url_for('login'))
        
    recipes = user_manager.get_user_recipes(session['email'])
    return render_template('userrecipes.html', recipes=recipes)

#**********************************************************************************

@app.route('/filter', methods=['GET'])
def filter_recipes():
    if 'email' not in session:
        flash('Please log in to view your recipes.')
        return redirect(url_for('login'))
    # Get the selected filters from query parameters
    selected_cuisines = request.args.getlist('cuisine')
    selected_times = request.args.getlist('time')

    filtered_recipes = recipe_manager.filter_recipes(selected_cuisines, selected_times)
    # Render the 'filter.html' template with the filtered recipes
    return render_template('filter.html', recipes=filtered_recipes)

#**********************************************************************************


@app.route('/delete-recipe/<id>', methods=['POST'])
def delete_recipe(id):
    if 'email' not in session:
        flash('Please log in to view your recipes.')
        return redirect(url_for('login'))
    recipe = recipe_manager.get_recipe(id)
    if recipe and recipe['imgLink']:
        photo_file_path = os.path.join('static', 'uploads', 
                                      os.path.basename(recipe['imgLink']))
        if os.path.exists(photo_file_path):
            os.remove(photo_file_path)

    recipe_manager.delete_recipe(id)
    
    if 'email' in session:
        user_manager.remove_recipe_from_user(session['email'], id)

    return redirect(url_for('your_recipes'))
#**********************************************************************************

@app.route('/editrecipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if 'email' not in session:
        flash('Please log in to view your recipes.')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        photo = request.files.get('photo')
        photo_filename = None
        if photo:
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo.filename))
            photo_filename = f'../static/uploads/{photo.filename}'

        recipe_data = {
            'recipe_name': request.form['recipeName'],
            'category': request.form['category'],
            'cuisine': request.form['cuisine'],
            'ingredients': [{"name": n, "measurement": m} 
                          for n, m in zip(request.form.getlist('ingredientName[]'),
                                        request.form.getlist('ingredientMeasurement[]'))],
            'instructions': request.form['instructions'],
            'time': request.form['time']
        }
        recipe_manager.update_recipe(recipe_id, recipe_data, photo_filename)
        return redirect(url_for('home'))  # Redirect after saving

    # Handle GET request to load the edit form
    recipe = recipe_manager.get_recipe(recipe_id)
    if recipe:
        return render_template('editrecipe.html', recipe=recipe)
    
    return "Recipe not found", 404

#**********************************************************************************

@app.route("/logout", methods=["GET", "POST"])
def logout():
    # Check if user is logged in
    if 'email' in session:
        # Remove email from session
        session.pop('email')
    
    return redirect(url_for('index'))


#**********************************************************************************

if __name__ == '__main__':
    app.run(debug=True)
