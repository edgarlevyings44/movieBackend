from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the Postgres connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://levy:P3f5ZTBxqLuukpXcaTLxFj26DoTtHh1l@dpg-cnaaa96v3ddc73d9b7p0-a.oregon-postgres.render.com/dbmovie_kcu8'

# Create the SQLAlchemy instance with the engine
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
@app.route('/')
def home():
    # Create a new user and add it to the database
    new_user = User(username='John Doe')
    db.session.add(new_user)
    db.session.commit()
    return 'User added to the database!'

if __name__ == '__main__':
    app.run(debug=True)