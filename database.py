import json

class Database:
    def __init__(self, recipe_file='recipes.json', user_file='users.json',category_file='categories.json'):
        self.recipe_file = recipe_file
        self.user_file = user_file
        self.category_file=category_file

    def load_json(self, filename):
        with open(filename, 'r+') as f:
            return json.load(f)

    def save_json(self, filename, data):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
