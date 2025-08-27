# 객체 지향 프로그래밍(OOP)

# 1. 절차지향 프로그래밍

# 1.1. 차량 1
car_company_1 = "Ferrari"
car_detail_1 = [{"color": "White"}, {"horsepower": 400}, {"price": 8000}]

# 1.2. 차량 2
car_company_2 = "BMW"
car_detail_2 = [{"color": "Black"}, {"horsepower": 270}, {"price": 5000}]

# 1.3. 차량 3
car_company_3 = "Audi"
car_detail_3 = [{"color": "Silver"}, {"horsepower": 300}, {"price": 6000}]

# 1.4. 출력
print(car_company_1)
print(car_detail_1)
print(car_company_2)
print(car_detail_2)
print(car_company_3)
print(car_detail_3)

print()

# 2. 리스트 구조
car_company_list = ["Ferrari", "BMW", "Audi"]
car_detail_list = [
    {"color": "White", "horsepower": 400, "price": 8000},
    {"color": "Black", "horsepower": 270, "price": 5000},
    {"color": "Silver", "horsepower": 300, "price": 6000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()

# 3. 딕셔너리 구조
car_dicts = [
    {
        "car_company": "Ferrari",
        "car_detail": {
            "color": "White",
            "horsepower": 400,
            "price": 8000,
        },
    },
    {
        "car_company": "BMW",
        "car_detail": {
            "color": "Black",
            "horsepower": 270,
            "price": 5000,
        },
    },
    {
        "car_company": "Audi",
        "car_detail": {
            "color": "Silver",
            "horsepower": 300,
            "price": 6000,
        },
    },
]

del car_dicts[1]

print(car_dicts)

print()

# 4. 클래스 구조


class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  # 문자열 출력문(사용자 레벨 정보)
        return f"str: {self._company}: {self._details}"

    def __repr__(self):  # 객체 정보 출력문(개발자 레벨 정보)
        return f"repr: {self._company}: {self._details}"


car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("BMW", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

car_list = [car1, car2, car3]

print(car_list)

for x in car_list:
    print(x)

for x in car_list:
    print(x.__dict__)

print()
