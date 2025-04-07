# 모듈 함수 예제
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def pow(x, y):
    return x**y


print("imported module_example")  # 이렇게 모듈 실행시 무언가 출력되면 안됨

# __name__ 사용
if __name__ == "__main__":  # 이 파일이 직접 실행되면 __name__은 "__main__"이 됨
    print("module_example was run directly")
