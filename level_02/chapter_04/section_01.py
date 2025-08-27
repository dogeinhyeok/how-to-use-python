# Magic Method(Special Method)
"""
> 매직 메소드(Magic Method)는 파이썬에서 특별한 기능을 수행하는 메소드입니다.
> 이중 밑줄(__)로 시작하고 끝나는 메소드로, 파이썬 인터프리터가 특정 상황에서 자동으로 호출합니다.
> 예: __init__, __str__, __add__, __len__ 등
> 매직 메소드를 통해 클래스에 연산자 오버로딩, 문자열 표현, 반복자 기능 등을 구현할 수 있습니다.
"""

# 1. 기본형
print(int)
print(float)
print()

# 2. 모든 속성 및 메소드 출력
print(f"dir(int): {dir(int)}")
print(f"dir(float): {dir(float)}")
print()

# 3. 매직 메소드 사용 예시
n = 10
print(n + 100)
print(n.__add__(100))
print(n.__doc__)  # 문서화 문자열
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))
print()


# 4. 매직 메소드 오버로딩
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"Fruit Class Info: {self._name}, {self._price}"

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price

    def __le__(self, x):
        print("Called >> __le__")
        return self._price <= x._price

    def __ge__(self, x):
        print("Called >> __ge__")
        return self._price >= x._price


# 5. 매직 메소드 출력
s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)
print(s1._price + s2._price)
print(s1.__add__(s2))
print(s1 + s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)
print()
