from database import Database
import json

class RecipeManager:
    def __init__(self, db: Database):
        self.db = db




    def get_next_id(self):
        # Load existing recipes and find the next available ID
        with open('id.json', 'r') as f:
            data = json.load(f)

            data['last_id'] = str(int(data['last_id']) + 1)
            with open('id.json', 'w') as file:
                json.dump(data, file, indent=4)
            return data['last_id']
        

    def add_recipe(self, recipe_data, photo_filename=None,new_id=None):
        data = self.db.load_json(self.db.recipe_file)
        # new_id = self.get_next_id()
        new_recipe = {
            "id": new_id,
            "recipe_name": recipe_data['recipe_name'],
            "categoryName": recipe_data['category'],
            "cuisine": recipe_data['cuisine'],
            "ingredients": recipe_data['ingredients'],
            "instructions": recipe_data['instructions'],
            "time": recipe_data['time'],
            "imgLink": photo_filename
        }
        data['recipes'].append(new_recipe)
        self.db.save_json(self.db.recipe_file, data)

    def get_recipe(self, recipe_id):
        data = self.db.load_json(self.db.recipe_file)
        return next((r for r in data['recipes'] if r['id'] == recipe_id), None)

    def update_recipe(self, recipe_id, recipe_data, photo_filename=None):
        data = self.db.load_json(self.db.recipe_file)
        for recipe in data['recipes']:
            if recipe['id'] == recipe_id:
                recipe.update({
                    "recipe_name": recipe_data['recipe_name'],
                    "categoryName": recipe_data['category'],
                    "cuisine": recipe_data['cuisine'],
                    "ingredients": recipe_data['ingredients'],
                    "instructions": recipe_data['instructions'],
                    "time": recipe_data['time']
                })
                if photo_filename:
                    recipe['imgLink'] = photo_filename
                break
        self.db.save_json(self.db.recipe_file, data)

    def delete_recipe(self, recipe_id):
        data = self.db.load_json(self.db.recipe_file)
        data['recipes'] = [r for r in data['recipes'] if r['id'] != recipe_id]
        self.db.save_json(self.db.recipe_file, data)

    def filter_recipes(self, cuisines=None, times=None):
        data = self.db.load_json(self.db.recipe_file)
        if not cuisines and not times:
            return []
        return [r for r in data['recipes'] if 
                (not cuisines or r['cuisine'] in cuisines) and
                (not times or r['time'] in times)]
