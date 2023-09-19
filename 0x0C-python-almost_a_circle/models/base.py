import json
import csv


class Base:
    """Base class for all geometric shapes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs:
            obj_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Base: An instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_str = file.read()
                obj_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize and save a list of objects to a CSV file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            if list_objs is None:
                list_objs = []
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                row_data = {name: getattr(obj, name) for name in fieldnames}
                writer.writerow(row_data)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize and load a list of objects from a CSV file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            reader = csv.DictReader(file, fieldnames=fieldnames)
            obj_list = []
            for row in reader:
                row = {k: int(v) for k, v in row.items()}
                obj_list.append(cls.create(**row))
            return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw Rectangles and Squares.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        import turtle
        from random import randint

        turtle.Screen().bgcolor("white")
        turtle.speed(10)

        colors = ["red", "blue", "green", "purple", "pink", "yellow", "orange"]

        for shape in list_rectangles:
            turtle.penup()
            turtle.goto(randint(-300, 300), randint(-300, 300))
            turtle.pendown()
            turtle.color(colors[randint(0, 6)])
            for _ in range(2):
                turtle.forward(shape.width)
                turtle.right(90)
                turtle.forward(shape.height)
                turtle.right(90)

        for shape in list_squares:
            turtle.penup()
            turtle.goto(randint(-300, 300), randint(-300, 300))
            turtle.pendown()
            turtle.color(colors[randint(0, 6)])
            for _ in range
