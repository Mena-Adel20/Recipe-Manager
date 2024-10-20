from datetime import datetime
from database import Database
import json
class UserManager:
    def __init__(self, db: Database):
        self.db = db

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

    def add_recipe_to_user(self, email, recipe_id):
        data = self.db.load_json(self.db.user_file)
        for user in data['users']:
            if user['email'] == email:
                user['recipes'].append(str(recipe_id))
                break
        self.db.save_json(self.db.user_file, data)

    def get_user_recipes(self, email):
        user_data = self.db.load_json(self.db.user_file)
        recipe_data = self.db.load_json(self.db.recipe_file)
        
        user_recipe_ids = next((user['recipes'] for user in user_data['users'] 
                              if user['email'] == email), [])
        return [r for r in recipe_data['recipes'] if r['id'] in user_recipe_ids]

    def remove_recipe_from_user(self, email, recipe_id):
        data = self.db.load_json(self.db.user_file)
        for user in data['users']:
            if user['email'] == email:
                user['recipes'] = [r for r in user['recipes'] if r != recipe_id]
                break
        self.db.save_json(self.db.user_file, data)
