import math


class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        for _ in range(self.length):
            print("*" * self.width)

    def invert(self):
        self.length, self.width = self.width, self.length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def double(self):
        self.length *= 2
        self.width *= 2

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

    def print_dim(self):
        print(f"Length: {self.length}, Width: {self.width}")

    def get_dim(self):
        return (self.length, self.width)

    def combine(self, other):
        self.length += other.length
        self.width += other.width

    def get_hypot(self):
        return math.sqrt(self.length**2 + self.width**2)


# Testing Box class
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

box1.print_dim()
box2.print_dim()
box3.print_dim()

# Checking equality
print("box1 == box2:", box1 == box2)
print("box1 == box3:", box1 == box3)

# Combining and doubling
box1.combine(box3)
print("After combining box3 into box1:")
box1.print_dim()

box2.double()
print("After doubling box2:")
box2.print_dim()

# Combining doubled box2 into box1
box1.combine(box2)
print("After combining box2 into box1:")
box1.print_dim()
print("Redering box with current dimensions")
box1.print_dim()
box1.render()
box2.print_dim()
box2.render()
box3.print_dim()
box3.render()
