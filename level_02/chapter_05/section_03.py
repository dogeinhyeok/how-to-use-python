from types import MappingProxyType
from dis import dis
from unicodedata import name

# Dict 및 Set 심화

# 1. immutable Dict
d = {'key1': 'value1'}

# 1.1. Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print()

# 1.2. 수정 불가
# d_frozen['key2'] = 'value2'  # TypeError 발생

# 1.3. 수정 가능
d['key2'] = 'value2'

# 2. Set 집합 자료형(순서 X, 중복 X)
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 2.1. 추가 가능
s1.add('Melon')
print(s1)
print()

# 2.2. 추가 불가
# s5.add('Melon')  # TypeError 발생
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 2.3. 선언 최적화
print('------')
print(dis('{10}'))
print('------')
print(dis('set([10])'))

# 3. 지능형 집합(Comprehending Set)
print('------')
print({name(chr(i), '') for i in range(0, 256)})  # 0~255 범위의 모든 유니코드 문자 집합 출력
