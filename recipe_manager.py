from database import Database
import json,os

class RecipeManager:
    def __init__(self, db: Database):
        self.db = db

        
#************************************************************************************
    def add_recipe(self, recipe_data, photo_filename=None,new_id=None):
        data = self.db.load_json(self.db.recipe_file)
        # creat new object to recipe 
        new_recipe = {
            "id": new_id,
            "recipe_name": recipe_data['recipe_name'],
            "categoryName": recipe_data['category'],
            "cuisine": recipe_data['cuisine'],
            "ingredients": recipe_data['ingredients'],
            "instructions": recipe_data['instructions'],
            "time": recipe_data['time']+" minutes",
            "imgLink": photo_filename
        }
        data['recipes'].append(new_recipe)
        self.db.save_json(self.db.recipe_file, data)
#************************************************************************************

    def get_recipes_Category(self, category_name):
        data = self.db.load_json(self.db.recipe_file)
        filtered_recipes = []
        # Iterate over each recipe in the recipes data
        for recipe in data["recipes"]:
            # Check if the category of the recipe matches the provided category name
            if recipe["categoryName"] == category_name:
                filtered_recipes.append(recipe)
        return filtered_recipes
#************************************************************************************
# function to get object recipe by id 
    def get_recipe(self, recipe_id):
        data = self.db.load_json(self.db.recipe_file)
        for r in data['recipes']:
                if r['id'] == recipe_id:
                    return r
        return None
#************************************************************************************
#function to update recipe take all data from back then update all values that changes and save it
#if the user change the image it first delete the old image from the local and then save the new image
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
                    photo_file_path = os.path.join('static', 'uploads', 
                                            os.path.basename(recipe['imgLink']))
                    if os.path.exists(photo_file_path):
                        os.remove(photo_file_path)
                    recipe['imgLink'] = photo_filename
                break
        self.db.save_json(self.db.recipe_file, data)

#************************************************************************************
# This function creates a new list updated_recipes and adds each recipe from data['recipes'] that does not match the recipe_id. 
# Finally, it assigns the new list back to data['recipes'].
    def delete_recipe(self, recipe_id):
        data = self.db.load_json(self.db.recipe_file)
        updated_recipes = []
        for r in data['recipes']:
            if r['id'] != recipe_id:
                updated_recipes.append(r)
        data['recipes'] = updated_recipes
        self.db.save_json(self.db.recipe_file, data)

#************************************************************************************

# function to filter recipes based on time and cuisine
# (done using check boxes so you can fitler only by (time or cuisine ) or by time and cuisine tigther
    def filter_recipes(self, cuisines=None, times=None):
        # if ther is null reutrn empty  to avoid load data
        if not cuisines and not times:
            return []
        filtered_recipes = []

        data = self.db.load_json(self.db.recipe_file)
        for r in data['recipes']:
            if (r['cuisine'] in cuisines) or (r['time'] in times):
                filtered_recipes.append(r)
        
        return filtered_recipes