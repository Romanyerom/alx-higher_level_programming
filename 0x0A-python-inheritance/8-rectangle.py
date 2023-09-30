#!/usr/bin/python3
"""
This module defines two classes: BaseGeometry and Rectangle.

BaseGeometry provides basic geometric operations.
Rectangle is a subclass of BaseGeometry and represents a rectangle.
"""


class BaseGeometry:
    """
    BaseGeometry class provides basic geometric operations.

    Methods:
    - area(self): Raises an exception with the
    message 'area() is not implemented'.
    - integer_validator(self, name, value):
    Validates that 'value' is a positive integer.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        This method is meant to be overridden by subclasses.

        Raises:
        - Exception: Always raises an exception with
        the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer.

        Args:
        - name (str): The name of the value being validated.
        - value (int): The value to be validated.

        Raises:
        - TypeError: If 'value' is not an integer.
        - ValueError: If 'value' is less than or equal to 0.

        """
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
    - __init__(self, width, height): Initializes
    a Rectangle instance with width and height.
      Validates that 'width' and 'height' are positive integers.

    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Raises:
        - TypeError: If 'width' or 'height' is not an integer.
        - ValueError: If 'width' or 'height' is less than or equal to 0.

        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
