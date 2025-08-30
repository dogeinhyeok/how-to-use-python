# 1. 파이썬 변수 범위(scope)

# 1.1. 예제 1: 함수 인자
def func_v1(a):
    print(a)
    # print(b)  # 예외: 지역변수 참조 불가


# 1.2. 예제 2: 전역변수
b = 20


def func_v2(a):
    print(a)
    print(b)


func_v2(10)

# 1.3. 예제 3: 지역변수
c = 30


def func_v3(a):
    c = 40
    print(a)
    print(c)  # 지역 변수 사용


def func_v3_2(a):
    global c
    print(a)
    print(c)  # 전역 변수 사용
    c = 40


print('>>', c)
func_v3(10)
print('---')
func_v3_2(10)
print('>>>', c)
print()

# 2. 클로저(Closure): 안쪽 함수가 바깥쪽 함수의 변수를 기억해서 나중에 사용할 수 있게 되는 것
"""
> 클로저가 되려면:
> 1. 함수 안에 함수가 있어야 하고
> 2. 바깥쪽 함수가 안쪽 함수를 반환해야 합니다
"""


def outer():
    a = 100  # 바깥쪽 함수의 변수

    def inner():
        return a + 100  # 안쪽 함수가 바깥쪽 함수의 변수 사용

    return inner  # 함수를 반환


# 2.1. 클래스 이용(클로저 사용하지 않음)
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, v):
        self.series.append(v)
        print('inner >> {} / {}'.format(self.series, len(self.series)))
        return sum(self.series) / len(self.series)


averager_cls = Averager()

print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))
print()


# 2.2. 클로저 사용
def closure_ex1():
    series = []  # 바깥쪽 함수의 변수

    def averager(v):
        series.append(v)  # 안쪽 함수가 바깥쪽 함수의 변수 사용
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager  # 함수를 반환


avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))
print(avg_closure1(70))
print()


# 2.3. 잘못된 클로저 사용
def closure_ex2():
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total  # 변수를 수정할 때는 nonlocal이 필요
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()

print(avg_closure2(10))
print(avg_closure2(30))
print(avg_closure2(50))
print(avg_closure2(70))
print()
