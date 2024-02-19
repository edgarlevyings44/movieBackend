# items.py

from models.item import Item
from db import db

def create_item(name):
    new_item = Item(name=name)
    db.session.add(new_item)
    db.session.commit()
    return new_item

def get_all_items():
    return Item.query.all()
