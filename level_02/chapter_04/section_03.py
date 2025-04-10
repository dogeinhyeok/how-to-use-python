# Magic Method(Special Method)
from collections import namedtuple  # 네임드 튜플
from math import sqrt  # 제곱근

# 1. 일반적인 튜플
point1 = (1.0, 5.0)
point2 = (2.5, 1.5)
length1 = sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
print(length1)
print("---")

# 2. 네임드 튜플
Point = namedtuple("Point", "x y")
point3 = Point(1.0, 5.0)
point4 = Point(2.5, 1.5)
length2 = sqrt((point3.x - point4.x) ** 2 + (point3.y - point4.y) ** 2)
print(f"d({point3}, {point4}) = {length2:.2f}")
print("---")

# 3. 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("Point", "x, y")
Point3 = namedtuple("Point", "x y")
Point4 = namedtuple("Point", "x y x class", rename=True)  # Default: False
temp_dict = {"x": 10, "y": 20}
temp = [52, 38]

print(Point1)
print(Point2)
print(Point3)
print(Point4)
print("---")

# 4. 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(25, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print("---")

# 5. 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)
print("---")

# 6. _fields, _make, _asdict
print(p1._fields, p2._fields, p3._fields)
print("---")

# 7. _asdict(): OrderedDict 반환
print(p1._asdict())
print(p4._asdict())
print("---")

# 8. 실 사용 실습
Classes = namedtuple("Classes", ["rank", "number"])

# 8.1. 그룹 리스트 선언
numbers = [str(n) for n in range(1, 6)]
ranks = "A B C".split()
print(numbers)
print(ranks)
print("---")

# 8.2. 리스트 컴프리헨션
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)
print("---")

# 8.3. 리스트 컴프리헨션(추천 방법)
students2 = [
    Classes(rank, number)
    for rank in "A B C".split()  # 바깥쪽 루프가 나중에 순회를 완료
    for number in [str(n) for n in range(1, 6)]  # 안쪽 루프가 먼저 순회를 완료
]
for student in students2:
    print(student)
