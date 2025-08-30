import time


# 데코레이터: 함수를 수정하지 않고 추가 기능을 제공하는 함수

# 1. 클로저를 사용한 데코레이터 패턴

def perf_clock(func):
    def perf_clocked(*args):
        st = time.perf_counter()  # 함수 시작 시간
        result = func(*args)  # 함수 실행
        et = time.perf_counter()  # 함수 종료 시간
        name = func.__name__  # 실행 함수명
        arg_str = ', '.join(repr(arg) for arg in args)  # 함수 매개변수
        print('[%0.5fs] %s(%s) -> %r' % (et - st, name, arg_str, result))
        return result
    return perf_clocked


@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


print('Called Decorator -> time_func')
time_func(1.5)
print('Called Decorator -> sum_func')
sum_func(100, 200, 300, 400, 500)
print()
