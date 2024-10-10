import json
from datetime import datetime

class User:
    def __init__(self, filename, email):
        self.filename = filename
        self.email = email
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_user(self, password, username):
    # Load existing user data from file
        try:
            with open(self.filename, 'r') as infile:
                # Check if file is empty
                if infile.read().strip():  # If the file is not empty
                    infile.seek(0)  # Go back to the beginning of the file after the check
                    data = json.load(infile)
                else:
                    data = []  # Initialize empty list if file is empty
        except json.JSONDecodeError:
            data = []  # If file is empty or invalid, initialize empty list

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