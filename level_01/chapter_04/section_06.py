# 집합 자료형(Set)

# 1. 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, "Pen", "Cap", "Plate"])
e = {"foo", "bar", "baz", "foo", "qux"}
f = {42, "foo", (1, 2, 3)}

print("a:", type(a), a)
print("b:", type(b), b)
print("c:", type(c), c)
print("d:", type(d), d)
print("e:", type(e), e)
print("f:", type(f), f)

# 2. 튜플 변환(set -> tuple)
t = tuple(b)
print("t:", type(t), t)
print("t:", t[0], t[1:3])
print()

# 3. 리스트 변환(set -> list)
list1 = list(c)
list2 = list(e)
print("list1:", list1)
print("list2:", list2)
print()

# 4. 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print()

# 5. 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 5.1. 교집합
print("s1 & s2:", s1 & s2)
print("s1 & s2:", s1.intersection(s2))

# 5.2. 합집합
print("s1 | s2:", s1 | s2)
print("s1 | s2:", s1.union(s2))

# 5.3. 차집합
print("s1 - s2:", s1 - s2)
print("s1 - s2:", s1.difference(s2))

# 5.4. 중복 제거 확인
print("s1 & s2:", s1.isdisjoint(s2))

# 5.5. 부분 집합 확인
print("subset:", s1.issubset(s2))
print("superset:", s1.issuperset(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print("s1:", s1)
s1.remove(2)  # 없는 값 제거 시 에러 발생
s1.discard(3)  # 없는 값 제거 시 에러 발생하지 않음
print("s1:", s1)
s1.clear()
print("s1:", s1)
print()
