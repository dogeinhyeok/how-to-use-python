# for 구문

# 1. 시퀀스 반복
"""
> for <변수> in <시퀀스>:
>     <실행문>
"""
for v1 in range(10):
    print("v1 is", v1)
print()

for v2 in range(1, 11):  # 1 ~ 10
    print("v2 is :", v2)
print()

for v3 in range(1, 11, 3):  # 1 ~ 10, 3씩 증가
    print("v3 is :", v3)
print()

# 2. 시퀀스 반복
sum1 = 0
for v in range(1, 1001):
    sum1 = sum1 + v
print("1 ~ 1000 sum:", sum1)
print("1 ~ 1000 sum:", sum(range(1, 1001)))
print("1 ~ 1000 4의 배수의 합:", sum(range(4, 1001, 4)))
print()

# 3. Iterables 자료형 반복
"""
> 타입: 문자열, 리스트, 튜플, 딕셔너리...
> 함수: range, reversed, enumerate, filter, map, zip...
"""

# 3.1. 예제 1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]
for n in names:
    print("You are", n)
print()

# 3.2. 예제 2
lotto_numbers = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers:
    print("Current number:", n)
word = "Beautiful"
print()

# 3.3. 예제 3
for s in word:
    print("word:", s)
print()

# 3.4. 예제 4
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul",
}
for k in my_info:
    print(f"key: {k}")
for v in my_info.values():
    print(f"value: {v}")
for k, v in my_info.items():
    print(f"key: {k}, value: {v}")
print()

# 3.5. 예제 5
name = "FineApple"
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.lower())
print()

# 4. break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for n in numbers:
    if n == 34:
        print("Found: 34!")
        break
    else:
        print("Not found: ", n)
print()

# 5. continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    print("current type:", type(v))
print()

# 6. for - else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for n in numbers:
    if n == 55:
        print("Found: 55")
        break
else:
    print("Not found: 55")
print()

# 7. 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print("{:4d}".format(i * j), end="")
    print()

# 변환 예제
name2 = "Aceman"
print("Reversed:", reversed(name2))
print("List:", list(reversed(name2)))
print("Tuple:", tuple(reversed(name2)))
print("Set", set(reversed(name2)))
print()
