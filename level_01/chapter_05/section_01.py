# if 구문

# 1. 기본 형식
print(type(True))  # 0이 아닌 수, 문자열, 리스트, 튜플, 딕셔너리, 집합 등
print(type(False))  # 0, None, 빈 문자열, 빈 리스트, 빈 튜플, 빈 딕셔너리, 빈 집합 등
print()

# 2.1. 기본 형식 예시 1
if True:
    print("Good")
if False:
    print("Bad")

# 2.2. 기본 형식 예시 2
if True:
    print("Good")
else:
    print("Bad")
print()

# 3. 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 3.1. 양변이 같은 경우 참
print(x == y)

# 3.2. 양변이 다를 때 참
print(x != y)

# 3.3. 좌변이 클 때 참
print(x > y)

# 3.4. 좌변이 크거나 같을 때 참
print(x >= y)

# 3.5. 우변이 클 때 참
print(x < y)

# 3.6. 우변이 크거나 같을 때 참
print(x <= y)
print()

# 4. 예제
city = ""
if city:
    print("You are in", city)
else:
    print("Please enter your city")
city = "Seoul"
if city:
    print("You are in", city)
else:
    print("Please enter your city")
print()

# 5. 논리 연산자(and, or, not)
a = 75
b = 40
c = 50
print("and:", a > b and b > c)
print("or:", a > b or b > c)
print("not:", not a > b)
print(not False)
print()

# 6. 산술, 관계, 논리 우선순위(산술 > 관계 > 논리)
print("e1:", 3 + 12 > 7 + 3)
print("e2:", 5 + 10 * 3 > 7 + 3 * 20)
print("e3:", 5 + 10 > 3 and 7 + 3 == 10)
print("e4:", 5 + 10 > 0 and not 7 + 3 == 10)
print()

# 6.1. 예제 1
score1 = 90
score2 = "A"
if score1 >= 90 and score2 == "A":
    print("Pass")
else:
    print("Fail")
print()

# 6.2. 예제 2
id1 = "vip"
id2 = "admin"
grade = "platinum"
if id1 == "vip" or id2 == "admin":
    print("관리자 입장")
if id2 == "admin" and grade == "platinum":
    print("최상위 관리자")
print()

# 7. 다중 조건문
num = 75
if num >= 90:
    print("Grade : A")
elif num >= 80:
    print("Grade : B")
elif num >= 70:
    print("Grade : C")
else:
    print("과락")
print()

# 8. 중첩 조건문
grade = "A"
total = 95

if grade == "A":
    if total >= 90:
        print("장학금 100%")
    elif total >= 80:
        print("장학금 80%")
    else:
        print("장학금 50%")
else:
    print("장학금 없음")
print()

# 9. in, not in
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name": "Lee", "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values())
print()
