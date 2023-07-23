import pickle

class Shape:

    def __init__(self):

        self.shape_type = ""

    def Show(self):

        pass

    def Save(self, filename):

        with open(filename, "wb") as f:

            pickle.dump(self, f)

    def Load(filename):

        with open(filename, "rb") as f:

            return pickle.load(f)

class Square(Shape):

    def __init__(self, x, y, side_length):

        super().__init__()

        self.x = x

import pickle

class Shape:

    def __init__(self):

        self.shape_type = ""

    def Show(self):

        pass

    def Save(self, filename):

        with open(filename, "wb") as f:

            pickle.dump(self, f)

    def Load(filename):

        with open(filename, "rb") as f:

            return pickle.load(f)

class Square(Shape):

    def __init__(self, x, y, side_length):

        super().__init__()

        self.x = x

        self.y = y

        self.side_length = side_length

        self.shape_type = "square"

    def Show(self):

        print(f"Square: x={self.x}, y={self.y}, side_length={self.side_length}")

class Rectangle(Shape):

    def __init__(self, x, y, width, height):

        super().__init__()

        self.x = x

        self.y = y

        self.width = width

        self.height = height

        self.shape_type = "rectangle"

def Show(self):

        print(f"Rectangle: x={self.x}, y={self.y}, width={self.width}, height={self.height}")

class Circle(Shape):

    def __init__(self, x, y, radius):

        super().__init__()

        self.x = x

        self.y = y

        self.radius = radius

        self.shape_type = "circle"

def Show(self):

    print(f"Circle: x={self.x}, y={self.y}, radius={self.radius}")

shapes = [Square(10, 10, 20), Rectangle(30, 30, 40, 50), Circle(60, 60, 30)]

for shape in shapes:

    shape.Show()

shape.Save(f"{shape.shape_type}.pickle")

loaded_shapes = []

for shape_type in ["square", "rectangle", "circle"]:

    loaded_shapes.append(Shape.Load(f"{shape_type}.pickle"))
# self.y=y

for shape in loaded_shapes:

    # shape.Show()self.y = y

    # self.side_length = side_length

    # self.shape_type = "square"

    def Show(self):

        print(f"Square: x={self.x}, y={self.y}, side_length={self.side_length}")

        class Rectangle(Shape):

            def __init__(self, x, y, width, height):

                super().__init__()

        self.x = x

        self.y = y

        self.width = width

        self.height = height

        self.shape_type = "rectangle"

def Show(self):

    print(f"Rectangle: x={self.x}, y={self.y}, width={self.width}, height={self.height}")

class Circle(Shape):

    def __init__(self, x, y, radius):

        super().__init__()

        self.x = x

        self.y = y

        self.radius = radius

        self.shape_type = "circle"

def Show(self):

    print(f"Circle: x={self.x}, y={self.y}, radius={self.radius}")

shapes = [Square(10, 10, 20), Rectangle(30, 30, 40, 50), Circle(60, 60, 30)]

for shape in shapes:

    shape.Show()

shape.Save(f"{shape.shape_type}.pickle")

loaded_shapes = []

for shape_type in ["square", "rectangle", "circle"]:

    loaded_shapes.append(Shape.Load(f"{shape_type}.pickle"))

for shape in loaded_shapes:

    shape.Show()