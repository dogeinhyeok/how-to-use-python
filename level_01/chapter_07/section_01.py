# 클래스


# 1. 예제 1
class Dog:  # object 상속
    # 클래스 변수(모든 인스턴스가 공유하는 속성)
    species = "firstdog"

    # 초기화/인스턴스 변수(개별 속성)
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1.1. 클래스 정보
print(Dog)
print()

# 1.2. 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 1.3. 비교(둘이 다른 인스턴스)
print(a == b, id(a), id(b))
print()

# 1.4. 클래스 내부 속성 확인
print("dog1:", a.__dict__)
print("dog2:", b.__dict__)
print()

# 1.5. 인스턴스 속성 확인
print(f"{a.name} is {a.age} and {b.name} is {b.age}")
if a.species == "firstdog":
    print(f"{a.name} is a {a.species}")
print()

# 1.6. 클래스 변수
print(Dog.species)
print(a.species)
print(b.species)
print()


# 2. 예제 2
class SelfTest:
    def func1():
        print("Func1 called")

    def func2(self):
        print(id(self))
        print("Func2 called")


f = SelfTest()  # 인스턴스 생성

# 2.1. id 호출
print(id(f))
print()

# 2.2. 인스턴스 메서드 호출(전역 함수)
f.func2()

# 2.3. 클래스 메서드 호출
SelfTest.func1()
SelfTest.func2(f)
print()


# 3. 예제 3
class Warehouse:
    # 클래스 변수
    stock_num = 0  # 재고

    # 생성자
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    # 소멸자
    def __del__(self):
        Warehouse.stock_num -= 1


# 3.1. 인스턴스 생성
user1 = Warehouse("Lee")
user2 = Warehouse("Cho")

print(Warehouse.stock_num)
print(f"id: {id(user1)}, user1: {user1.name}, stock_num: {user1.stock_num}")
print(f"id: {id(user2)}, user2: {user2.name}, stock_num: {user2.stock_num}")
print()

Warehouse.stock_num = 50
print(Warehouse.stock_num)
print(f"id: {id(user1)}, user1: {user1.name}, stock_num: {user1.stock_num}")
print(f"id: {id(user2)}, user2: {user2.name}, stock_num: {user2.stock_num}")
print()

# 3.2. 인스턴스 삭제
del user1  # 소멸자 호출
print("after:", Warehouse.stock_num)  # 50 - 1
print()


# 4. 예제 4
class Dog:
    # 클래스 속성
    species = "firstdog"

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# 4.1. 인스턴스 생성
c = Dog("july", 4)
d = Dog("Marry", 10)

# 4.2. 메소드 호출
print(c.info())
print(d.info())
print(c.speak("Wal Wal"))
print(d.speak("Mung Mung"))
print()
