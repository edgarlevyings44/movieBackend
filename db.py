# db.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://products_online_user:tf9vwR7YLnL05JLdQf0Nt6wZBk2Yeq5n@dpg-cn11pq5a73kc73eerac0-a.oregon-postgres.render.com/products_online'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
