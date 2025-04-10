# Magic Method(Special Method)
class Vector(object):
    def __init__(self, *args):
        """Create a vector, example: v = Vector(5, 10)"""
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """Returns the vector information"""
        return f"Vector({self._x}, {self._y})"

    def __add__(self, other):
        """Returns the vector addition of self and other"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, scalar):
        """Returns the vector multiplication of self and scalar"""
        return Vector(self._x * scalar, self._y * scalar)

    def __bool__(self):
        return bool(max(self._x, self._y))


# 1. Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 34)
v3 = Vector()

# 2. 매직 메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))
