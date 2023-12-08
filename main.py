from math import sin, pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        print(f"Point with coordinates: x = {self.x}; y = {self.y}")


class Segment(Point):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)
        self.end = Point(x2, y2)

    def info(self):
        print(f"Segment: from x1 = {self.x}, y1 = {self.y} to x2 = {self.end.x}, y2 = {self.end.y}")

    def lenght(self):
        print("segment's lenght:", ((self.x - self.end.x) ** 2 + (self.y - self.end.y) ** 2) ** 0.5)


class GeometricFigure:
    def __init__(self):
        pass

    def info(self):
        print("GeometricFigures:")


class Polygon(GeometricFigure, Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        print(f"Polygon with one point and coordinates: {self.x} and {self.y}")


class Quadrilateral(GeometricFigure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        print("Perimeter:", self.a + self.b + self.c + self.d)

    def info(self):
        print(f"Quadrilateral with sides: a = {self.a}; b = {self.b};"
              f" c = {self.c}; d = {self.d}")

    def count_angles(self):
        print("Count angles: 4")


class Parallelogram(Quadrilateral):
    def __init__(self, a, b, angle):
        super().__init__(a, b, a, b)
        self.angle = angle

    def area(self):
        print("Area:", self.a * self.b * sin(self.angle))

    def info(self):
        print(f"Parallelogram with sides and angle: a = {self.a}; b = {self.b}; angle = {self.angle}")


class Rectangle(Parallelogram):
    def __init__(self, a, b):
        super().__init__(a, b, pi / 2)

    def info(self):
        print(f"Rectangle with sides: a = {self.a}; b = {self.b}")


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def info(self):
        print(f"Square with side: a = {self.a}")


class Triangle(GeometricFigure):
    def __init__(self, a, b, c, angle):
        self.a = a
        self.b = b
        self.c = c
        self.angle = angle

    def area(self):
        print("Area:", 0.5 * self.a * self.b * sin(self.angle))

    def perimeter(self):
        print("Perimeter:", self.a + self.b + self.c)

    def info(self):
        print(f"Triangle with sides and angle: a = {self.a}; b = {self.b}; c = {self.c}; angle = {self.angle}")

    def count_angles(self):
        print("Count angles: 3")


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a, pi / 3)

    def info(self):
        print(f"EquilateralTriangle with side and angle: a = {self.a}; angle = {self.angle}")


class Circumference(GeometricFigure):
    def __init__(self, d):
        self.d = d

    def info(self):
        print(f"Circumference with diameter: d = {self.d}")

    def radius(self):
        print("Radius:", self.d / 2)

    def area(self):
        print("Area:", (pi * ((self.d / 2) ** 2)))

    def lenght_circumference(self):
        print("Lenght_circumference:", pi * self.d)


class Ellipse(Circumference):
    def __init__(self, d, d1):
        super().__init__(d)
        self.d1 = d1

    def info(self):
        print(f"Ellipse with diameters: d = {self.d}; d1 = {self.d1}")

    def radius(self):
        print("Radius:", self.d / 2, self.d1 / 2)

    def area(self):
        print("Area:", (pi * ((self.d / 2) * (self.d1 / 2))))


p = Point(3, 4)
p.info()
s = Segment(3, 4, -3, -4)
s.lenght()
s.info()
g = GeometricFigure()
g.info()
pol = Polygon(3, 4)
pol.info()
q = Quadrilateral(10, 20, 30, 40)
q.info()
q.perimeter()
q.count_angles()
par = Parallelogram(10, 20, pi / 6)
par.info()
par.perimeter()
par.area()
par.count_angles()
r = Rectangle(10, 20)
r.info()
r.area()
r.perimeter()
r.count_angles()
s = Square(10)
s.info()
s.area()
s.perimeter()
s.count_angles()
t = Triangle(10, 20, 30, pi / 3)
t.info()
t.area()
t.perimeter()
t.count_angles()
et = EquilateralTriangle(30)
et.info()
et.area()
et.perimeter()
et.count_angles()
c = Circumference(20)
c.info()
c.radius()
c.area()
c.lenght_circumference()
e = Ellipse(20, 30)
e.info()
e.radius()
e.area()
