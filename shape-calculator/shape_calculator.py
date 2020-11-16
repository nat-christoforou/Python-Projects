"""A Shape Calculator."""


class Rectangle:
    """Create a Rectangle class."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height attributes."""
        self.width = width
        self.height = height

    def set_width(self, width):
        """Set the width of the Rectangle."""
        self.width = width

    def set_height(self, height):
        """Set the height of the Rectangle."""
        self.height = height

    def get_area(self):
        """Calculate the area of the Rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Calculate the diagonal of the Rectangle."""
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        """Represent the shape of the Rectangle using lines of '*'."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        output = ('*' * self.width + "\n") * self.height
        return output

    def get_amount_inside(self, other):
        """Get number of times that Rectangle1 within Rectangle2."""
        return (self.width // other.width) * (self.height // other.height)

    def __repr__(self):
        """Represent Rectangle as a string."""
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    """Create a Square class as subclass of Rectangle."""

    def __init__(self, side):
        """Initialize Square with side attribute."""
        super().__init__(side, side)

    def set_side(self, side):
        """Set the sides of the Square."""
        self.width = side
        self.height = side

    def set_width(self, width):
        """Set the sides of the Square."""
        super().set_width(width)
        self.height = width

    def set_height(self, height):
        """Set the sides of the Square."""
        super().set_height(height)
        self.width = height

    def __repr__(self):
        """Represent Square as a string."""
        return "Square(side={})".format(self.width)
