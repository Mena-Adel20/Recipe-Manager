from datetime import datetime
from database import Database
import json
class UserManager:
    def __init__(self, db: Database):
        self.db = db
#************************************************************************************

    def add_user(self, email, password, username):
        try:
            data = self.db.load_json(self.db.user_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {'users': []}

        if any(user['email'] == email for user in data['users']):
            return 'Email already exists. Please use a different email address.'

        new_user = {
            "email": email,
            "pass": password,
            "user": username,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "recipes": []
        }
        data['users'].append(new_user)
        self.db.save_json(self.db.user_file, data)
        return None

#************************************************************************************

    # save recipe id to user
    def add_recipe_to_user(self, email, recipe_id):
        data = self.db.load_json(self.db.user_file)
        #find the user that add recipe and add id of recipe in his list of recipes 
        for user in data['users']:
            if user['email'] == email:
                user['recipes'].append(str(recipe_id))
                break
        self.db.save_json(self.db.user_file, data)
#************************************************************************************

    def get_user_recipes(self, email):
        user_data = self.db.load_json(self.db.user_file)
        recipe_data = self.db.load_json(self.db.recipe_file)
        # first get user form data and then get the list of his recipes  
        user_recipe_ids = []
        for user in user_data['users']:
            if user['email'] == email:
                user_recipe_ids = user['recipes']
                break  
        # Now filter the recipes based on the user_recipe_ids
        filtered_recipes = []
        for r in recipe_data['recipes']:
            if r['id'] in user_recipe_ids:
                filtered_recipes.append(r)

        return filtered_recipes
#************************************************************************************

#this function to remove a specific recipe from a user's list of recipes in a JSON data structure that stores user information. 
    def remove_recipe_from_user(self, email, recipe_id):
        data = self.db.load_json(self.db.user_file)
        for user in data['users']:
            if user['email'] == email:
                updated_recipes = []
                for r in user['recipes']:
                    if r != recipe_id:  
                        updated_recipes.append(r)  
                user['recipes'] = updated_recipes  
                break
        self.db.save_json(self.db.user_file, data)
