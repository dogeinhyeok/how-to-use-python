# 언더스코어(_)

# 1. 언더스코어 언팩킹(Unpacking): 값을 무시하고 싶을 때 사용합니다
x, _, y = (1, 2, 3)
print(x, y)

a, *_, b = (1, 2, 3, 4, 5)
print(a, b)

for _ in range(3):
    pass

for _, val in enumerate(range(3)):
    print(val)

print()

# 2. 접근지정자(Access Modifier): 변수, 메서드, 클래스의 접근 권한을 제한합니다
"""
> name : public
> _name : protected
> __name : private
> 파이썬은 접근 지정자의 강제성이 없습니다. 명명 규칙만 존재합니다.
"""


class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        self._z = 0


a = SampleA()
a.x = 1
print(f"x: {a.x}")
print(f"y: {a._SampleA__y}")  # Name Mangling으로 직접 접근을 제한합니다.
print(f"z: {a._z}")
a._SampleA__y = 10  # Private 변수도 억지로 접근하여 변경 가능합니다.
print()


# 3. 메소드 활용 Getter, Setter
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value


b = SampleB()

b.x = 1
b.set_y(2)

print(f"x: {b.x}")
print(f"y: {b.get_y()}")
print()
