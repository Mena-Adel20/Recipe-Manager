from flask import Flask, request, jsonify
from user import User  # Importing the User class from the separate file

app = Flask("main")

# Define the filename where user data will be stored
FILENAME = 'users_data.json'

@app.route('/signup', methods=['POST'])
def signup():
    # extracts JSON data from the body of the incoming HTTP request
    data = request.get_json()
    
    # This line checks whether the required fields are  in  data 
    if not all(key in data for key in ['email', 'password', 'username']):
        return jsonify({'error': 'Missing parameters'}), 400
    
    # Create a User object and try to add the user
    user_manager = User(filename=FILENAME, email=data['email'])
    result = user_manager.add_user(password=data['password'], username=data['username'])

    if result is None:
        return jsonify({'message': 'User signed up successfully'}), 200
    else:
        return jsonify({'error': result}), 400


if __name__ == '__main__':
    app.run(debug=True)
