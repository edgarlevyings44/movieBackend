from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://levy:P3f5ZTBxqLuukpXcaTLxFj26DoTtHh1l@dpg-cnaaa96v3ddc73d9b7p0-a.oregon-postgres.render.com/dbmovie_kcu8'
db = SQLAlchemy(app)