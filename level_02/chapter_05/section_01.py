# 컨테이너 자료형
import array

# 1. 지능형 리스트(Comprehending Lists)
chars = "+_)(*&^%$#@!)"
code_list1 = []
for s in chars:
    code_list1.append(ord(s))
print(code_list1)
print()

# 2. 지능형 리스트(Comprehending Lists)
code_list2 = [ord(s) for s in chars]  # 주로 사용하는 방법
print(code_list2)
print()

# 3. 지능형 리스트(Comprehending Lists) + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]  # 주로 사용하는 방법
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list3)
print(code_list4)
print()

# 3.1. 전체 출력(유니코드)
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print()

# 3.2. 전체 출력(문자)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
print()

# 4. Generator 생성
tuple_g = (ord(s) for s in chars)  # 튜플 형태로 생성(메모리 절약)
array_g = array.array("I", (ord(s) for s in chars))  # 배열 형태로 생성
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist())
print()

# 4.1. Generator 생성 예제
print(("%s" % c + str(n) for c in ["A", "B"] for n in range(1, 4)))
for s in ("%s" % c + str(n) for c in ["A", "B"] for n in range(1, 4)):
    print(s)
print()

# 5. 리스트 주의
marks1 = [["~"] * 3 for _ in range(4)]
marks2 = [["~"] * 3] * 4

print(marks1)  # 각 리스트의 주소가 다름
print(marks2)  # 모든 리스트의 주소가 같음
print()

# 5.1. 수정
marks1[0][1] = "X"
marks2[0][1] = "X"

print(marks1)
print(marks2)  # 모든 리스트의 [1] 인덱스 값이 모두 덮어씌워짐
print()

# 5.2. 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])  # 각 리스트의 주소가 같음
print()
