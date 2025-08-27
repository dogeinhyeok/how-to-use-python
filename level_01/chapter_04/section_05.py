# 딕셔너리 자료형(Dictionary)

# 1. 선언
a = {"name": "Kim", "phone": "01033337777", "birth": "870514"}
b = {0: "Hello Python"}
c = {"arr": [1, 2, 3, 4]}
d = {"Name": "Niceman", "City": "Seoul", "Age": 33, "Grade": "A", "Status": True}
e = dict(
    [
        ("Name", "Niceman"),
        ("City", "Seoul"),
        ("Age", 33),
        ("Grade", "A"),
        ("Status", True),
    ]
)
f = dict(Name="Niceman", City="Seoul", Age=33, Grade="A", Status=True)

print("a:", type(a), a)
print("b:", type(b), b)
print("c:", type(c), c)
print("d:", type(d), d)
print("e:", type(e), e)
print("f:", type(f), f)
print()

# 2. 출력
print("a:", a["name"])  # 키가 없을때 에러 호출
print("a:", a.get("name"))  # 키가 없을때 None 호출
print("b:", b[0])
print("b:", b.get(0))
print("f:", f.get("City"))
print("f:", f.get("Age"))
print()

# 3. 딕셔너리 추가
a["name"] = "seoul"
print("a:", a)
a["name"] = [1, 2, 3]
print("a:", a)
print()

# 4. 딕셔너리 길이
print("a:", len(a))
print("b:", len(b))
print()

# 5. 딕셔너리 함수
print("a:", a.keys())
print("b:", b.keys())
print("a:", list(a.keys()))
print("b:", list(b.keys()))
print("a:", a.values())
print("b:", b.values())
print("a:", list(a.values()))
print("b:", list(b.values()))
print("a:", a.items())
print("b:", b.items())
print("a:", list(a.items()))
print("b:", list(b.items()))
print("a:", a.pop("name"))
print("a:", a)
print("c:", c.pop("arr"))
print("c:", c)
print("f:", f.popitem())
print("f:", f)
print("a:", "birth" in a)
print("d:", "City" in d)
print()

# 6. 딕셔너리 수정
a["test"] = "test_dict"
print("a:", a)

a.update(birth="910904")
print("a:", a)

temp = {"address": "Busan"}
a.update(temp)
print("a:", a)
print()
