#!/usr/bin/python3

class Rectangle:
    """
    A class representing a rectangle.

    This class provides methods and attributes to work with rectangles.

    Attributes:
        number_of_instances (int): Class attribute to keep track of instances.
        print_symbol (str): Class attribute for symbol used to represent the rectangle.

    Methods:
        __init__(self, width=0, height=0): Constructor method to initialize a rectangle instance.
        area(self): Calculate the area of the rectangle.
        perimeter(self): Calculate the perimeter of the rectangle.
        __str__(self): Get a string representation of the rectangle.
        __repr__(self): Get a formal string representation of the rectangle.
        __del__(self): Destructor method to clean up when a rectangle is deleted.
    """

    number_of_instances = 0  # Class attribute to keep track of instances
    print_symbol = "#"  # Class attribute for symbol used to represent the rectangle

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment upon instantiation

    @property
    def width(self):
        """
        int: The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Get a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        return rectangle.rstrip()  # Remove trailing newline

    def __repr__(self):
        """
        Get a formal string representation of the rectangle.

        Returns:
            str: A formal string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Clean up when a rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1  # Decrement upon deletion
        print("Bye rectangle...")
