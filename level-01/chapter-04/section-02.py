# 문자열

# 1. 문자열 생성
str_1 = "I am Python"
str_2 = "Python"
str_3 = """How are you?"""
str_4 = """Thank you!"""

print(type(str_1), type(str_2), type(str_3), type(str_4))
print(len(str_1), len(str_2), len(str_3), len(str_4))
print()

# 2. 빈 문자열
str_t1 = ""
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))
print()

# 3. 이스케이프 문자
"""
> \n : 줄바꿈
> \t : 탭
> \\ : 문자열
> \' : 작은따옴표
> \" : 큰따옴표
> \000 : 널 문자
"""
print("I'm Back")
print("I\\m Back")
print("Hello\tWorld")
print("Hello\nWorld")
print()

# 4. Raw String
raw_s = r"D:\Python\Python310\python.exe"
print(raw_s)
print()

# 5. 멀티라인 입력
multi_str = """
String
Multi Line
Test
"""
print(multi_str)
print()

# 6. 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print("y" in str_o1)
print("Y" in str_o1)
print("y" not in str_o1)
print()

# 7. 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print()

# 8. 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
str_py = "python is powerful"
print("Capitalize: ", str_py.capitalize())
print("endswith?: ", str_py.endswith("ful"))
print("startswith?: ", str_py.startswith("py"))
print("replace: ", str_py.replace("powerful", "awsome"))
print("sorted: ", sorted(str_py))
print("split: ", str_py.split(" "))
print()

# 9. 반복(시퀀스)
str_nice = "Nice Python"
print(dir(str_nice))
print()

# 9.1. 출력
for i in str_nice:
    print(i)
print()

# 9.2. 슬라이싱
print(str_nice[0:3])
print(str_nice[3:])
print(str_nice[: len(str_nice) - 1])
print(str_nice[1:9:2])
print(str_nice[-5:])
print(str_nice[1:-2])
print(str_nice[::2])
print(str_nice[::-1])
print()

# 10. 아스키 코드
a = "z"
print(ord(a))
print(chr(122))
