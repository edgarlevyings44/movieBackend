# Import the Flask class from the flask module
from flask import Flask, jsonify
from db import init_db
from controllers.item import create_item, get_all_items
from requests import request

# Create an instance of the Flask class
app = Flask(__name__)

# Load the configuration for the database
init_db(app)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

# Define a route for a custom page
@app.route('/about')
def about():
    return 'This is a simple Flask app created for demonstration purposes.'

# Define a route for a custom page
@app.route('/contact')
def contact():
    return 'This are our contacts.'

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        items = get_all_items()
        items_json = [{"id": item.id, "name": item.name} for item in items]
        return jsonify(items_json)

    elif request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        new_item = create_item(name)
        return jsonify({"id": new_item.id, "name": new_item.name})

# Run the app if this script is the main program
if __name__ == '__main__':
    app.run(debug=True)
