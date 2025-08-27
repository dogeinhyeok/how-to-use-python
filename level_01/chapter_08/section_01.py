# 예외처리의 이해

# 1. SyntaxError : 문법 오류
# print("error"))

# 2. NameError : 참조 변수 없음
"""
> a = 1
> b = 15
> print(c)
"""

# 3. ZeroDivisionError : 0으로 나누기
"""
> print(100 / 0)
"""

# 4. IndexError : 인덱스 범위 오류
"""
> x = [50, 70, 90]
> print(x[4])
"""

# 5. KeyError : 키 오류
"""
> dic = {"name": "Lee", "Age": 41, "City": "Busan"}
> print(dic["hobby"])
"""

# 6. AttributeError : 속성 오류
"""
> import time
> print(time.time2())
"""

# 7. ValueError : 값 오류
"""
> x = [10, 50, 90]
> x.remove(200)
"""

# 8. FileNotFoundError : 파일 없음
"""
> f = open("test.txt")
"""

# 9. TypeError : 타입 오류
"""
> x = [1, 2]
> y = (1, 2)
> z = "test"
> print(x + y)
> print(x + z)
"""

# 10. 예외 처리 기본
name = ["Kim", "Lee", "Park"]

# 10.1. 예제 1
try:
    z = "Cho"
    x = name.index(z)
    print(f"{z} Found it! {x + 1} is name")
except ValueError:  # 예외 발생 시 실행
    print("Not found it! - Occurred ValueError!")
print()

# 10.2. 예제 2
try:
    z = "Cho"
    x = name.index(z)
    print(f"{z} Found it! {x + 1} is name")
except ValueError as e:
    print(e)
    print("Not found it! - Occurred ValueError!")
else:  # 예외 발생 시 실행되지 않음
    print("Ok! else.")
finally:  # 예외 발생 여부 상관 없이 실행
    print("Ok! finally.")
print()

# 10.3. 예제 3
try:
    a = "Park"
    if a == "Kim":
        print("OK! Pass!")
    else:
        raise ValueError
except ValueError:
    print("Occurred! ValueError!")
else:
    print("Ok! else.")
print()
