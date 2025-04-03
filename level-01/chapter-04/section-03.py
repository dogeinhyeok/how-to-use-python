# 리스트 자료형(List)

# 1. 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, "Ace", "Base", "Captine"]
e = [1000, 10000, ["Ace", "Base", "Captine"]]
f = [21.42, "foobar", 3, 4, False, 3.14159]

# 2. 인덱싱
print("d:", type(d), d)
print("d:", d[1])
print("d:", d[0] + d[1] + d[1])
print("d:", d[-1])
print("e:", e[-1][1])
print("e:", list(e[-1][1]))
print()

# 3. 슬라이싱
"""
> c[1:4] → 인덱스 1에서 시작해서 인덱스 4 전에 멈춥니다 (인덱스 1, 2, 3 포함)
"""
print("d:", d[0:3])
print("d:", d[2:])
print("e:", e[-1][1:3])
print()

# 4. 리스트 연산
print("c + d:", c + d)
print("c * 3:", c * 3)
print("Test" + str(c[0]))
print()

# 5. 값 비교
print(c == c[:3] + c[3:])
print(c[:3])
print(c[3:])
print()

# 6. 값 접근
temp = c
print(temp, c)
print(id(temp))
print(id(c))
print()

# 7. 리스트 수정, 삭제
print("c:", c)
c[0] = 4
print("c:", c)
c[1:2] = ["a", "b", "c"]
print("c:", c)
c[1:3] = []
print("c:", c)
del c[1]
print("c:", c)
print()

# 8. 리스트 함수
a = [5, 2, 3, 1, 4]
print("a:", a)
a.append(10)
print("a:", a)
a.sort()
print("a:", a)
a.reverse()
print("a:", a)
print("a:", a.index(3))
a.insert(2, 7)
print("a:", a)
a.reverse()
print("a:", a)
a.remove(10)
print("a:", a)
print("a:", a.pop())
print("a:", a)
print("a:", a.pop())
print("a:", a)
print("a:", a.count(4))
ex = [8, 9]
a.extend(ex)
print("a:", a)

# 삭제 : remove, pop, del
while a:
    data = a.pop()
    print(data)
