# 객체 지향 프로그래밍(OOP)


class Car:
    """
    Car 클래스
    Author: 홍길동
    Date: 2025-04-09
    Description: Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):  # 문자열 출력문(사용자 레벨 정보)
        return f"str: {self._company}: {self._details}"

    def __repr__(self):  # 객체 정보 출력문(개발자 레벨 정보)
        return f"repr: {self._company}: {self._details}"

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print(f"Current ID: {id(self)}")
        print(f"Car Datail Info: {self._company} {self._details.get('price')}")


# 1. Self 의미
car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("BMW", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

# 2. ID 확인
print(id(car1))
print(id(car2))
print(id(car3))
print(car1._company == car2._company)  # 값 비교
print(car1 is car2)  # 객체 비교
print("---")

# 3. dir & __dict__ 확인
print(dir(car1))
print(dir(car2))
print(car1.__dict__)
print(car2.__dict__)
print("---")

# 4. Doctring
print(Car.__doc__)
print("---")

# 5. 인스턴스 함수 실행
car1.detail_info()
car2.detail_info()
print("---")

# 6. 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))
print("---")

# 7. 클래스 함수 실행
Car.detail_info(car1)
Car.detail_info(car1)
print("---")

# 8. 클래스 변수 접근
print(f"car_count: {car1.car_count}")
print(f"car_count: {Car.car_count}")
del car2
print(f"car_count: {car1.car_count}")
print(f"car_count: {Car.car_count}")
