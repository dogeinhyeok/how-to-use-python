# 함수
"""
> 함수는 프로그램에서 반복적으로 사용되는 기능을 묶어서 이름을 붙인 것
>
> def <함수이름>(<매개변수>):
>     <실행할 문장>
>     return <반환값>
"""


# 1. 매개변수가 필요하지 않은 함수
def func1():
    print("함수 호출")


# 2. 매개변수가 필요한 함수
def func2(a, b):
    print(f"a: {a}, b: {b}")


# 3. 결과값을 반환하지 않는 함수
def func3(x, y):
    print(f"x: {x}, y: {y}")


# 4. 결과값을 반환하는 함수
def func4(x, y):
    return x + y


# 5. 다중 반환(튜플 리턴)
def func_multiple_return(n):
    x = n * 10
    y = n * 20
    z = n * 30
    return x, y, z


# 6. 튜플 리턴
def func_tuple_return(n):
    x = n * 10
    y = n * 20
    z = n * 30
    return (x, y, z)


# 7. 리스트 리턴
def func_list_return(n):
    x = n * 10
    y = n * 20
    z = n * 30
    return [x, y, z]


# 8. 세트 리턴
def func_set_return(n):
    x = n * 10
    y = n * 20
    z = n * 10
    return {x, y, z}


# 9. 딕셔너리 리턴
def func_dict_return(n):
    x = n * 10
    y = n * 20
    z = n * 30
    return {"x": x, "y": y, "z": z}


# 10. 팩킹(*args)
"""
> 팩킹: 여러 개의 값을 하나의 변수로 묶어서 전달하는 것
> *args: 함수 호출 시 전달되는 여러 개의 인자들을 튜플로 묶어서 처리
"""


def func_packing_args(*args):  # *args: 여러 개의 인자를 튜플로 패킹
    for i, v in enumerate(args):
        print(f"args[{i}]: {v}")  # 패킹된 각 인자를 순차적으로 출력


# 11. 팩킹(**kwargs)
def func_packing_kwargs(**kwargs):  # **kwargs: 여러 개의 키워드 인자를 딕셔너리로 패킹
    for k, v in kwargs.items():
        print(f"kwargs[{k}]: {v}")  # 패킹된 각 키워드 인자를 순차적으로 출력


# 12. 혼합팩킹
def func_packing_mixed(arg1, arg2, *args, **kwargs):
    print(f"arg1: {arg1}, arg2: {arg2}")
    for i, v in enumerate(args):
        print(f"args[{i}]: {v}")
    for k, v in kwargs.items():
        print(f"kwargs[{k}]: {v}")


# 13. 중첩 함수
def nested_func(num):
    def func_in_func(num):  # 외부에서 호출 불가
        print(f"Inner func: {num}")

    print(f"Outer func: {num}")
    func_in_func(num + 100)


# 실행 함수 모음 (1 ~ 13)
func1()
func2(10, 20)
func3(100, 200)
print(f"x + y = {func4(10, 20)}")
print("---")
x, y, z = func_multiple_return(1)
print(f"x: {x}, y: {y}, z: {z}")
print(type(func_tuple_return(1)), func_tuple_return(1))
print(type(func_list_return(1)), func_list_return(1))
print(type(func_set_return(1)), func_set_return(1))
print(type(func_dict_return(1)), func_dict_return(1))
print("---")
func_packing_args(1, 2, 3, 4, 5)
func_packing_kwargs(a=1, b=2, c=3)
func_packing_mixed(1, 2, "Lee", "Kim", "Park", a=1, b=2, c=3)
print("---")
nested_func(100)
print("---")

# 14. 람다 함수
"""
> 람다 함수: 한 줄로 간단하게 함수를 정의하는 방법
>
> lambda <매개변수>: <표현식>
"""


def calculator(x, y, func):
    return func(x, y)


print(calculator(10, 3, lambda x, y: x + y))
print(calculator(10, 3, lambda x, y: x - y))
print(calculator(10, 3, lambda x, y: x * y))
print(calculator(10, 3, lambda x, y: x / y))
