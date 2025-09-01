# Variable scope

# 예제 1: 전역 변수 참조 - 함수 내에서 전역 변수를 읽기만 하는 경우
a = 10  # Global variable


def foo():
    print("Foo > ", a)


foo()

print('Global Function > ', a)
print()

# 예제 2: 지역 변수 우선 - 함수 내에서 같은 이름의 지역 변수가 전역 변수를 가림
b = 20


def bar():
    b = 30  # Local variable
    print("Bar > ", b)  # 로컬 변수 사용


bar()

print('Global Function > ', b)
print()

# 예제 3: 변수 할당 전 참조 오류 - 지역 변수 할당 전에 수정하려고 하면 예외 발생
c = 40


def foobar():
    # c = c + 10  # 아직 정의되지 않은 로컬 변수이므로 예외 발생
    print("Foobar > ", c)


foobar()

print('Global Function > ', c)
print()


# 예제 4: global 키워드 - 함수 내에서 전역 변수를 수정할 때 사용
d = 50


def barfoo():
    global d
    d = 60
    d += 100
    print("Barfoo > ", d)


barfoo()

print('Global Function > ', d)
print()


# 예제 5: 내부 함수가 외부 함수의 변수 e를 같은 메모리 주소로 참조하여 호출할 때마다 값이 누적됨
def outer():
    e = 70  # 메모리 주소값을 가지고 있는 변수

    def inner():  # 같은 메모리 주소를 계속 참조하고 있음
        nonlocal e  # 같은 메모리 주소에서 변수를 가져옴
        e += 10  # 같은 메모리 주소에서 값을 수정
        print("Inner > ", e)
    return inner


inner = outer()
inner()
inner()
print()


# 예제 6: locals() 함수 - 현재 함수의 지역 변수들을 딕셔너리로 반환
def func(var):
    x = 10

    def printer():
        print("func > ", "Printer Func Inner")
    print("locals > ", locals())  # 함수 내부의 변수 목록


func("Hi")
print()


# 예제 7: globals() 함수 - 전역 네임스페이스의 모든 변수들을 딕셔너리로 반환
print("globals > ", globals())  # 전역 변수 목록
print()


# 예제 8: globals() 딕셔너리를 통해 전역 변수를 동적으로 생성하고 출력
for i in range(1, 3):
    for j in range(1, 3):
        globals()['plus_{}_{}'.format(i, j)] = i + j
    print()

print(globals())
print("---")
print("i", i)
print("j", j)
print("plus_1_1", plus_1_1)  # noqa
print("plus_1_2", plus_1_2)  # noqa
print("plus_2_1", plus_2_1)  # noqa
print("plus_2_2", plus_2_2)  # noqa
print()
