# Property 활용 Getter, Setter

# 1. Property 데코레이터 기본 사용법
class SamepleA:
    def __init__(self):
        self.x = 0
        self.__y = 0  # private 변수

    # Getter
    @property
    def y(self):
        print("Getter y() called")
        return self.__y

    # Setter
    @y.setter
    def y(self, value):
        print("Setter y() called")
        self.__y = value

    # Deleter
    @y.deleter
    def y(self):
        print("Deleter y() called")
        del self.__y


a = SamepleA()
a.y = 2  # setter 호출
print(f"y: {a.y}")  # getter 호출
del a.y  # deleter 호출
print()


# 2. Property 데코레이터를 활용한 유효성 검증
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("0 이상의 값을 입력하세요.")
        self.__y = value

    @y.deleter
    def y(self):
        del self.__y


b = SampleB()
b.y = -5  # ValueError 발생
print()
