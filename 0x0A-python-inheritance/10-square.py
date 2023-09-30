#!/usr/bin/python3
"""This module defines three classes: BaseGeometry, Rectangle, and Square.

BaseGeometry provides basic geometric operations.
Rectangle is a subclass of BaseGeometry and represents a rectangle.
Square is a subclass of Rectangle and represents a square.

"""

class BaseGeometry:
    """
    BaseGeometry class provides basic geometric operations.

    Methods:
    - area(self): Raises an exception with the message
    'area() is not implemented'.
    - integer_validator(self, name, value): Validates
    that 'value' is a positive integer.

    """

    def area(self):
        """Raises an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    Rectangle class represents a rectangle
    and inherits from BaseGeometry.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): Initializes a Rectangle
    instance with width and height.
    Validates that 'width' and 'height' are positive integers.
    - area(self): Calculates and returns the area of the rectangle.
    - __str__(self): Returns a string representation of the
    Rectangle in the format '[Rectangle] <width>/<height>'.

    """

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the Rectangle
        in the format '[Rectangle] <width>/<height>'."""
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """
    Square class represents a square and inherits from Rectangle.

    Methods:
    - __init__(self, size): Initializes a Square instance with a size.
      Validates that 'size' is a positive integer.

    """

    def __init__(self, size):
        """Initializes a Square instance with a size."""
        super().__init__(size, size)
