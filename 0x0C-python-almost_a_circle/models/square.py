#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor for Square

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate Defaults to 0.
            y (int): The y-coordinate Defaults to 0.
            id (int): The id for the Square instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Update the attributes of the Square

        Args:
            *args: List of positional arguments.
            **kwargs: Dictionary of keyword arguments.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,  # Size is the same as width for Square
            "x": self.x,
            "y": self.y,
        }
