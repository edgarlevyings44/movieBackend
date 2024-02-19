# item.py
from db import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return f"Item(id={self.id}, name={self.name})"
