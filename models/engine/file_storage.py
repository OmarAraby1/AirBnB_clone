#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """A class that serializes instances to a JSON file and vice versa."""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects by <class name>.id

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets a new object in __objects with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to a JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

    def __init__(self):
        """Reloads objects from the file when the class is instantiated."""
        self.reload()
