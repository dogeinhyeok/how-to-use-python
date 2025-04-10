# 내장(Built-in) 함수

# 1. 절대값
print(abs(-3))

# 2. all, any : iterable 요소 검사(참, 거짓)
print(all([1, 2, 3]))
print(any([1, 2, 0]))

# 3. chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(67))
print(ord("C"))
print("---")

# 4. enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(["abc", "bcd", "efg"]):
    print(i + 1, name)
print("---")


# 5. filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))
print("---")

# 6. id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))
print("---")

# 7. len : 요소의 길이 반환
print(len("abcdefg"))
print(len([1, 2, 3, 4, 5, 6, 7]))
print("---")

# 8. max, min : 최대값, 최소값
print(max([1, 2, 3]))
print(max("python"))
print(min([1, 2, 3]))
print(min("python"))
print("---")


# 9. map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6])))
print("---")

# 10. pow: 제곱값 반환
print(pow(2, 10))
print("---")

# 11. range : 반복가능한 객체(iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))
print("---")

# 12. round : 반올림
print(round(6.5781, 2))
print(round(5.6))
print("---")

# 13. sorted : 반복가능한 객체(Iterable) 정렬 후 반환
print(sorted([6, 7, 4, 3, 1, 2]))
print(sorted(["p", "y", "t", "h", "o", "n"]))
print("---")

# 14. sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6, 7, 8, 9, 10]))
print(sum(range(1, 101)))
print("---")

# 15. type : 자료형 확인
print(type(3))
print(type({3, 4, 5}))
print(type(3.0))
print(type([1, 2, 3]))
print("---")

# 16. zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10, 20, 30], [40, 50, 60])))
print(type(list(zip([10, 20, 30], [40, 50, 60]))[0]))
print("---")
