#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

def get_storage_type():
    return 'db' if getenv('HBNB_TYPE_STORAGE') == 'db' else 'file'

def get_class_by_name(class_name):
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }
    return classes.get(class_name)

# This line should be after all the functions to prevent circular import
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

storage_t = get_storage_type()
