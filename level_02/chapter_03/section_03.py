# 객체 지향 프로그래밍(OOP)


class Car:
    """
    Car 클래스
    Author: 홍길동
    Date: 2025-04-09
    Description: Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  # 문자열 출력문(사용자 레벨 정보)
        return f"str: {self._company}: {self._details}"

    def __repr__(self):  # 객체 정보 출력문(개발자 레벨 정보)
        return f"repr: {self._company}: {self._details}"

    # Instance Method
    def detail_info(self):
        print(f"Current ID: {id(self)}")
        print(f"Car Datail Info: {self._company} {self._details.get('price')}")

    # Instance Method
    def get_price(self):
        return "Before Car Price -> company: {}, price: {}".format(
            self._company, self._details.get("price")
        )

    # Instance Method
    def get_price_culc(self):
        return "After Car Price -> company: {}, price: {}".format(
            self._company, self._details.get("price") * Car.price_per_raise
        )

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter a number greater than 1")
            return
        cls.price_per_raise = per
        print("Succeed! price increased.")

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == "BMW":
            return "This car is {}".format(inst._company)
        return "This car is not BMW."


# 1. Self 의미
car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("BMW", {"color": "Black", "horsepower": 270, "price": 5000})

# 2. 전체 정보
car1.detail_info()
car2.detail_info()
print("---")

# 3. 가격 정보
print(car1._details.get("price"))
print(car1._details["price"])
print("---")

# 4. 가격 인상
print(car1.get_price())
print(car2.get_price())
print("---")

# 4.1. 클래스 변수 사용
Car.price_per_raise = 1.4
print(car1.get_price_culc())
print(car2.get_price_culc())
print("---")

# 4.2.클래스 메소드 사용
"""
> 첫 번째 매개변수로 cls를 받음 (클래스 자체를 참조)
> 클래스 변수와 메소드에 접근 가능
> 인스턴스 변수에는 직접 접근 불가
"""
Car.raise_price(1.6)
print(car1.get_price_culc())
print(car2.get_price_culc())
print("---")

# 4.3. 스테틱 메소드 사용
"""
> 첫 번째 매개변수로 inst를 받음 (인스턴스 자체를 참조)
> 클래스나 인스턴스 변수에 직접 접근 불가
> 하지만 매개변수로 받은 인스턴스를 통해 접근 가능
"""
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
