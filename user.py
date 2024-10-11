
import json
from datetime import datetime

class User:
    def __init__(self, filename, email):
        self.filename = filename
        self.email = email
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Load existing user data from file
    def add_user(self, password, username):
        try:
            with open(self.filename, 'r') as infile:
                if infile.read().strip():
                    infile.seek(0)
                    data = json.load(infile)
                else:
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        # Check if email already exists
        for user in data:
            if user['email'] == self.email:
                return 'Email already exists. Please use a different email address.'

        # Create new user
        new_user = {"email": self.email, "pass": password, "user": username, "date": self.date, "favorites": []}
        data.append(new_user)

        # Write updated data back to file
        with open(self.filename, 'w') as outfile:
            json.dump(data, outfile, indent=4)

        return None