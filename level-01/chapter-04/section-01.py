import math

# 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합(시퀀스)
dict : 딕셔너리(키-값 쌍)
"""

# 1. 데이터 타입
str_var = "Python"
str_var2 = "Anaconda"
bool_var = True
float_var = 10.0
int_var = 7
list_var = [str_var, str_var2, bool_var, float_var, int_var]
dict_var = {"name": "Machine Learning", "version": 2.0}
tuple_var = (7, 8, 9)
set_var = {7, 8, 9}

# 2. 데이터 타입 출력
print(type(str_var))
print(type(str_var2))
print(type(bool_var))
print(type(float_var))
print(type(int_var))
print(type(list_var))
print(type(dict_var))
print(type(tuple_var))
print(type(set_var))
print()

# 3. 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : 거듭제곱
"""

# 4. 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777779999999999999999999999  # 자릿수 자동 확장

# 5. 정수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 6. 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

# 7. 연산 실습
i1 = 39
i2 = 939
f1 = 1.234
f2 = 3.939
big_int1 = 7777777777777777777777777777777777777777777
big_int2 = 9999999999999999999999999999999999999999999

# 7.1. +
print(">>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print()

# 7.2. *
print(">>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)
print()

# 8. 형 변환 실습
a = 3.0
b = 6
c = 0.7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))
print()

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True))  # True : 1, False : 0
print(float(True))  # True : 1.0, False : 0.0
print(complex(3))
print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3), 5**3)
print()

# 외부 모듈
print(math.pi)
print(math.ceil(5.1))  # 올림
print(math.floor(3.874))  # 내림
