def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number (default is 98).

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If a or b are not integers or floats.

    Example:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
