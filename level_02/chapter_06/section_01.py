from functools import reduce
from functools import partial
from operator import add
from operator import mul

# 일급 함수(일급 객체)
"""
> 파이썬 함수 특징
> 1. 런타임 초기화
> 2. 변수 할당 가능
> 3. 함수 인수 전달 가능
> 4. 함수 결과 반환 가능
"""


# 1. 팩토리얼 함수(재귀 사용): 5! = 5 * 4 * 3 * 2 * 1
def factorial(n):
    """Factorial Function -> n : int"""
    if n == 1:  # n < 2
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)
print()

# 2. 변수 할당
var_func = factorial

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))  # map으로 각 요소에 함수 적용
print()

# 3. 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)

# 3.1. map, filter
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])
print()

# 3.2. reduce: 여러 값을 순차적으로 결합하여 하나의 값으로 만드는 누적 연산 함수
print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))
print()

# 4. reduce에서 익명함수(lambda) 사용
print(reduce(lambda x, t: x + t, range(1, 11)))
print()

# 5. Callable: 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
print(callable(str), callable(list), callable(var_func), callable(factorial),
      callable(3.14))
print()

# 6. partial 사용법 : 인수 고정 -> 콜백 함수 사용
print(mul(10, 10))
five = partial(mul, 5)
print(five(10))
six = partial(five, 6)
print(six())
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))
print()
