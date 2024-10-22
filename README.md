# Recipe-Manager (Foodie)

Foodie website for discovering, and sharing recipes. With easy-to-follow instructions, ingredient lists, a variety of categories

- What does it do?
  Example: "This is a web project which allow user know how can prepare recipe. and user can update his recipe"
- What is the "new feature" which you have implemented that we haven't seen before?  
  Example: "reading from json file","adding to json file "sending values to the route to use it", "deleting from file" , "using jinja to display elemnts", "filter by two values".

## Prerequisites

Did you add any additional modules that someone needs to install (for instance anything in Python that you `pip install-ed`)?
List those here (if any).

Before running this project, ensure you have the following prerequisites installed:

- Python: Install Python(last version Python 3.12.7)
- Flask: You can install Flask using pip, Python's package installer. Run the following command:
  ` pip install Flask`
- Jinja in Visual Studio Code: Ensure you have Visual Studio Code installed. Jinja is a templating engine used by Flask, and it should be integrated into Visual Studio Code by default when you have the Python extension installed.
- run website write those commands: $env:FLASK_APP = "main.py" ===> flask run.

## Project Checklist

- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.
      Please provide the name of the module you are using in your app.
  - Module name: json , datetime, os
    [x] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to let the class initialize the object's attributes (note that `__init__()` doesn't count as a method). This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name for the class definition: database
    Line number(s) for the class definition: line 3 in database.
    Name of two properties: recipe_file, user_file,category_file
  - Name of two methods: load_json, save_json
    - File name and line numbers where the methods are used:load_json in ( main.py , line 61) - save_json in(recipe-manager.py , line 24 )
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It makes use of the reading and writing to the same file feature.
- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least
      one example of a conditional statement in your code.
  - File name:main.py, recipe-manager.py, user-manager.py .
  - Line number(s):26,33,36,41,49,54,104,.....
- [x] It contains loops. Please provide below the file name and the line number(s) of at least
      one example of a loop in your code.
  - File name:main.py, recipe-manager.py, user-manager.py .
  - Line number(s):31,40,48,63,73.....
- [x] It lets the user enter a value in a text box at some point.
      This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] It is styled using CSS.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code.
      In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.
