from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://avnadmin:AVNS_CfgBHmKoHZYY7KpD10G@pg-16ee9791-edgarlevy81-b97b.a.aivencloud.com:26711/defaultdb?sslmode=require'
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
@app.route('/')
def check():
	return 'Flask is working'


if __name__ == '__main__':
	app.run()
