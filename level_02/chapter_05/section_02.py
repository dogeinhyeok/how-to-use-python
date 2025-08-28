# 1. Tuple 자료형(Immutable, 순서 O, 중복 O, 수정 X, 읽기 전용)

# 1.1. 언패킹
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))
print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = range(1, 5)
print(x, y, rest)
print()

# 2. Mutable(가변) vs Immutable(불변)
tuple_l = (15, 20, 25)  # 튜플은 불변 객체
list_m = [15, 20, 25]  # 리스트는 가변 객체

print(tuple_l, id(tuple_l))
print(list_m, id(list_m))

tuple_l = tuple_l * 2
list_m = list_m * 2  # = 연산자는 새로운 객체를 생성하여 할당합니다

print(tuple_l, id(tuple_l))
print(list_m, id(list_m))

tuple_l *= 2
list_m *= 2  # 가변 객체의 경우, *= 연산자는 기존 객체를 수정합니다

print(tuple_l, id(tuple_l))  # 튜플은 불변 객체이므로 주소가 변경해야 값을 수정할 수 있음
print(list_m, id(list_m))  # 리스트는 가변 객체이므로 주소가 변경하지 않아도 값을 수정할 수 있음
print()

# 3. sort vs sorted

# 3.1. sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon',
          'strawberry', 'coconut']
print('sorted -', sorted(f_list))  # 기본 정렬
print('sorted -', sorted(f_list, reverse=True))  # 역순 정렬
print('sorted -', sorted(f_list, key=len))  # 길이순 정렬
print('sorted -', sorted(f_list, key=lambda x: x[-1]))  # 마지막 문자 순 정렬
print('sorted -', sorted(f_list, key=lambda x: x[-1],
                         reverse=True))  # 마지막 문자 역순 정렬
print()

# 3.2. sort : 정렬 후 기존 객체 정렬 (원본 변경)
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
print()

# 4. List vs Array 적합한 사용법

# 4.1. List : 융통성, 다양한 자료형, 범용적 사용

# 4.2. Array : 특정 자료형, 배열(리스트)과 거의 호환

# 5. 해시테이블 : Key에 Value를 저장하는 구조

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))  # 불변 객체만 해시 가능
# print(hash(t2))  # 가변 객체(리스트)는 해시 불가
print()

# 5.1. Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# 5.1.1. No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)
print()

# 5.1.2. Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)
print()

# 5.1.3. 잘못된 사용 예시
new_dict3 = {k: v for k, v in source}
print(new_dict3)  # 나중에 추가된 값으로 덮어씌워짐
print()
