import copy

# 1. 참조(Reference): 같은 리스트를 가리키므로 복사가 아닌 동일한 객체 공유
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print("예제 > ", id(a_list))
print("예제 > ", id(b_list))
b_list[2] = 4
print("예제 > ", a_list)
print("예제 > ", b_list)
print()

# 2. 얕은 복사(Shallow Copy): 리스트는 복사하지만 내부 중첩 리스트는 같은 주소값을 참조
c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print("예제 > ", id(c_list))
print("예제 > ", id(d_list))
print("예제 > ", id(c_list[3]))
print("예제 > ", id(d_list[3]))
d_list[2] = 4
d_list[3][2] = 7  # 원본도 변경됨: 내부 배열의 주소값이 같기 때문
print("예제 > ", c_list)
print("예제 > ", d_list)
print()

# 3. 깊은 복사(Deep Copy): 리스트와 내부 중첩 리스트까지 모두 새로운 주소값으로 완전히 복사
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)
print("예제 > ", id(e_list))
print("예제 > ", id(f_list))
print("예제 > ", id(e_list[3]))
print("예제 > ", id(f_list[3]))
f_list[2] = 4
f_list[3][2] = 7  # 원본은 변경되지 않음: 내부 배열의 주소값이 다르기 때문
print("예제 > ", e_list)
print("예제 > ", f_list)
print()
