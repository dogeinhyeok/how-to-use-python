import itertools

# 병행성(Concurrency): 한 컴퓨터가 동시 실행
# 병렬성(Parallelism): 여러 컴퓨터가 동시 실행


# 1. 제네레이터 예제
def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')


temp = iter(generator_ex1())

print(next(temp))
print("---")
print(next(temp))
print("---")
for v in generator_ex1():
    pass  # yield로 반환된 값을 무시
print()

# 1.1. Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]  # 리스트를 만들어야 하니까 모든 값을 다 계산
temp3 = (x * 3 for x in generator_ex1())  # 필요할 때마다 하나씩 제공하면 됨
print("---")
print(temp2)
print("---")
print(temp3)
print()

# 1.2. Generator Ex3(중요 함수)
gen1 = itertools.count(1, 2.5)  # 1부터 2.5씩 증가
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한 증가 가능
print()

# 2. 조건
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print(v)
print()

# 2.1. 필터 반대
gen3 = itertools.filterfalse(lambda x: x < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)
print()

# 2.2. 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 6)])

for v in gen4:
    print(v)
print()

# 3. 서로 다른 이터레이터 연결 1
gen5 = itertools.chain("ABCDE", range(1, 11, 2))
print(list(gen5))
print()

# 3.1. 서로 다른 이터레이터 연결 2
gen6 = itertools.chain(enumerate("ABCDE"))  # enumerate()가 각 문자에 인덱스 번호를 붙여줌
print(list(gen6))
print()

# 3.2. 개별
gen7 = itertools.product("AB", "12")  # product()는 여러 집합의 모든 가능한 조합을 생성
print(list(gen7))
print()

# 3.3. 그룹화
gen8 = itertools.groupby("AAABBCCCCDDEEE")
for chr, group in gen8:
    print(chr, " : ", list(group))
print()
