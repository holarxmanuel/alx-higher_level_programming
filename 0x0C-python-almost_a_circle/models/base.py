import json
import csv
import turtle


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                data = [getattr(obj, attr) for attr in obj.to_dictionary()]
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                instance = cls(*map(int, row))
                instances.append(instance)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.Screen().title("Turtle Drawing")
        turtle.speed(0)
        turtle.bgcolor("white")
        turtle.penup()
        turtle.hideturtle()

        for rect in list_rectangles:
            turtle.color("blue")
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.penup()

        for square in list_squares:
            turtle.color("red")
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.penup()

        turtle.exitonclick()
