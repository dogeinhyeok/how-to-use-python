import sys

# Print 사용법

# 0. scape 코드
"""
> \n : 줄바꿈
> \t : 탭
> \\ : 문자열
> \' : 작은따옴표
> \" : 큰따옴표
> \000 : 널 문자
"""

# 1. 기본 출력
"""
> 문자열 출력 방법
> 큰따옴표(""), 작은따옴표(''), 큰따옴표 3개(""" """)
"""
print("Python Start!")
print("Python Start!")
print("""Python Start!""")
print("""Python Start!""")
print()

# 2. separator 옵션
"""
> 쉼표(,)로 구분된 문자열을 출력할 때 사용
> sep 옵션은 이어서 출력할 때 사이에 출력할 구분자를 변경할 때 사용
> 기본값은 띄어쓰기( )
"""
print("P", "Y", "T", "H", "O", "N")
print("010", "7777", "1234", sep="-")
print("python", "google.com", sep="@")
print()

# 3. end 옵션
"""
> 줄바꿈을 하지 않고 문자열을 이어서 출력하는 옵션
> end 옵션은 줄바꿈 대신 출력할 문자열을 지정할 때 사용
"""
print("Welcome To", end=" ")
print("IT News", end=" ")
print("Web Site")
print()

# 4. file 옵션
"""
> 출력 결과를 파일로 저장할 때 사용
> file 옵션은 파일 객체를 지정할 때 사용
"""
print("Learn Python", file=sys.stdout)
print()

# 5. format 옵션(d : 3, s : 'python', f : 3.141592)
print("%s %s" % ("one", "two"))
print("{} {}".format("one", "two"))
print("{1} {0}".format("one", "two"))
print()

# 6. 공백채우기
print("%10s" % ("nice"))
print("{:>10}".format("nice"))

print("%-10s" % ("nice"))
print("{:10}".format("nice"))

print("{:^10}".format("nice"))

print("{:_>10}".format("nice"))
print("{:_<10}".format("nice"))
print("{:_^10}".format("nice"))
print()

# 7. 문자열 자르기
print("%.5s" % ("nice"))
print("%.5s" % ("pythonstudy"))

print("{:10.5}".format("nice"))
print("{:10.5}".format("pythonstudy"))

print("{:_<10.5}".format("nice"))
print("{:_<10.5}".format("pythonstudy"))
print()

# 8. 숫자 출력
print("%d %d" % (1, 2))
print("{} {}".format(1, 2))

print("%4d" % (42))
print("{:4d}".format(42))
print()

# 9. 실수 출력
print("%1f" % (3.1415926535897932384626433832795028))
print("%1.18f" % (3.1415926535897932384626433832795028))

print("%f" % (3.1415926535897932384626433832795028))
print("{:f}".format(3.1415926535897932384626433832795028))

print("%06.2f" % (3.1415926535897932384626433832795028))
print("{:06.2f}".format(3.1415926535897932384626433832795028))
print()
