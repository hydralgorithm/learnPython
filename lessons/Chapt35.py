# property = decorator used to define a method as property

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter method
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    # Getter method
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    # Setter method
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
    # Setter method
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")
    # Deleter method
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted!")
    # Deleter method
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted!")


rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = -1

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
