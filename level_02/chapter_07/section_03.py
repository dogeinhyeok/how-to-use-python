from inspect import getgeneratorstate

# 코루틴(Coroutine): 비동기 작업을 병렬로 수행하는 기술


# 1. 코루틴 예제 1
def coroutine1():
    print(">>> coroutine started.")  # 1단계: 시작
    i = yield  # 2단계: 여기서 멈춤 (값을 받을 준비)
    print(">>> coroutine received: {}".format(i))  # 3단계: 받은 값 출력


# 1.1. 제네레이터 선언
cr1 = coroutine1()
print(cr1, type(cr1))

# 1.2. yield 지점까지 서브루틴 수행
next(cr1)

# 1.3. 기본 전달 값 None
try:
    cr1.send(100)
except StopIteration:
    print("StopIteration")
print()


# 2. 코루틴 예제 2
def coroutine2(x):
    print(">>> coroutine started: {}".format(x))
    y = yield x  # x(10)를 반환하고 y를 받을 준비
    print(">>> coroutine received: {}".format(y))
    z = yield x + y  # x + y(10 + 100 = 110)를 반환하고 z를 받을 준비
    print(">>> coroutine received: {}".format(z))
    yield z


cr3 = coroutine2(10)
print(getgeneratorstate(cr3))
print(next(cr3))
print(cr3.send(100))
print()


# 3. 코루틴 예제 3
def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print()

# 4. 코루틴 예제
t2 = generator1()

print(list(t2))


def generator2():
    yield from 'AB'
    yield from range(1, 4)


t3 = generator2()


print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print()
