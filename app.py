from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://products_online_user:tf9vwR7YLnL05JLdQf0Nt6wZBk2Yeq5n@dpg-cn11pq5a73kc73eerac0-a.oregon-postgres.render.com/products_online'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
@app.route('/')
def home():
    # Create a new user and add it to the database
    new_user = User(username='JohnDoe')
    db.session.add(new_user)
    db.session.commit()

    return 'User added to the database!'

if __name__ == '__main__':
    app.run(debug=True)
