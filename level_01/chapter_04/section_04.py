# 튜플 자료형(Tuple)
"""
> 변경되지 않는 데이터, 딕셔너리 키, 함수 인자로 활용
> - 좌표 값 (x, y)
> - 날짜 정보 (년, 월, 일)
> - RGB 색상 값 (r, g, b)
> - 설정 정보나 상수 데이터
> - 함수에서 여러 값 반환 (return name, age, score)
"""

# 1. 선언
a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, "Ace", "Base", "Captine")
e = (100, 1000, ("Ace", "Base", "Captine"))

# 2. 인덱싱
print("d:", d[1])
print("d:", d[0] + d[1] + d[1])
print("d:", d[-1])
print("e:", e[-1])
print("e:", e[-1][1])
print("e:", list(e[-1][1]))
print()

# 3. 튜플은 수정되지 않습니다
# d[0] = 1500

# 4. 슬라이싱
print("d:", d[0:3])
print("d:", d[2:])
print("d:", e[-1][1])
print()

# 5. 튜플 연산
print("c + d", c + d)
print("c * 3", c * 3)
print()

# 6. 튜플 함수
a = (5, 2, 3, 1, 4)
print("a:", a)
print("a:", a.index(3))
print("a:", a.count(2))
print()

# 7. 팩킹(Packing)
t = ("foo", "bar", "baz", "qux")
print(t)
print(t[0])
print(t[-1])
print()

# 8. 언팩킹(Unpacking)
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print()

# 9. 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = (4,)
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
print()
