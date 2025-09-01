from functools import reduce

# 1. lambda: 함수를 변수에 할당하거나 다른 함수의 인자로 전달할 때 사용
cul = lambda a, b, c: a * b + c  # noqa
print("lambda > ", cul(10, 15, 20))
print()

# 2. map: 리스트의 모든 요소에 동일한 연산을 수행할 때 사용
digits = [x * 10 for x in range(1, 11)]
print("digits > ", digits)
result = list(map(lambda i: i ** 2, digits))
print("result > ", result)


# 2.1. map 함수 사용 버전
def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)


print("also_square > ", list(also_square(digits)))
print()

# 3. filter: 리스트에서 특정 조건을 만족하는 요소들만 선택할 때 사용
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, digits2))
print("result > ", result)


# 3.1. filter 함수 사용 버전
def also_even(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)


print("also_even > ", list(also_even(digits2)))
print()

# 4. reduce: 여러 값들을 하나씩 처리해서 최종 결과 하나를 만드는 함수
"""
> 처음: x = 1, y = 2 → 1 + 2 = 3
> 다음: x = 3, y = 3 → 3 + 3 = 6
> 다음: x = 6, y = 4 → 6 + 4 = 10
"""
digits3 = [x for x in range(1, 101)]
result = reduce(lambda x, y: x + y, digits3)
print("result > ", result)


# 4.1. reduce 함수 사용 버전
def also_add(nums):
    def add(x, y):
        return x + y
    return reduce(add, nums)


print("also_add > ", also_add(digits3))
print()
