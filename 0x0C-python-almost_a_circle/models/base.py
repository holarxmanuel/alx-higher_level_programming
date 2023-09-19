#!/usr/bin/python3
""" Base module """
import json
import csv


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a new instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from a JSON file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                data = cls.from_json_string(file.read())
            return [cls.create(**d) for d in data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes list_objs to CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(getattr(obj, name) for name in fieldnames)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes list_objs from CSV file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                data = [dict(map(int, row.items())) for row in reader]
            return [cls.create(**d) for d in data]
        except FileNotFoundError:
            return []
