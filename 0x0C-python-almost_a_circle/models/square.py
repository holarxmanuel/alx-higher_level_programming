#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor for Square

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position. Defaults to 0.
            y (int): The y-coordinate of the square's position. Defaults to 0.
            id (int): The id for the Square instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update the Square instance attributes

        Args:
            *args: List of non-keyword arguments.
            **kwargs: Double pointer to a dictionary with keyworded arguments.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """Override the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
