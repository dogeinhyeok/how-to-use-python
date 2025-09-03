# Type 함수

# 1. type 동적 클래스 생성 예제

# Name(이름), Bases(상속), Dict(속성)
s1 = type("Sample1", (), {})
print(s1)
print(type(s1))
print(s1.__base__)
print()


# 2. type 동적 생성 + 상속
class Parent1:
    pass


s2 = type("Sample2", (Parent1,), dict(attr1=100, attr2="hi"))
print(s2)
print(type(s2))
print(s2.__base__)
print(s2.attr1, s2.attr2)
print()


# 3. type 동적 생성 + 메소드 추가
class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n

    def mul(self, m, n):
        return m * n


e1 = SampleEx()
print(e1.attr1, e1.attr2)
print(e1.add(10, 20), e1.mul(10, 20))
print()


# 3.1. type 함수로 동적 클래스 생성 및 테스트
s3 = type("Sample3", (object,), {
    'attr1': 30,
    'attr2': 100,
    'add': lambda x, y: x + y,
    'mul': lambda x, y: x * y
})

print(s3.attr1, s3.attr2)
print(s3.add(10, 20), s3.mul(10, 20))
print()
