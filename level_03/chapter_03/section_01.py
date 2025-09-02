import contextlib
import time
import os

# 프로젝트 루트 디렉토리 찾기
current_file = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
testfile4 = os.path.join(project_root, 'output', 'testfile4.txt')

# Context Manager: 파이썬에서 리소스를 안전하게 관리하는 패턴


# 1. 파일 처리 Context Manager
@contextlib.contextmanager
def my_file_writer(file_path, method):
    file = open(file_path, method)  # __init__
    yield file  # __enter__
    file.close()  # __exit__


# 1.1. with 문으로 리소스의 획득과 해제를 자동으로 처리합니다
with my_file_writer(testfile4, "w") as file:
    file.write("Context Manager Test4.\nContext Manager Test4.")


# 2. 실행 시간 측정 Context Manager
@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()  # __init__
    try:  # __enter__
        yield start
    except BaseException as e:
        print(f"Logging exception: {msg}: {e}")
        raise e
    else:  # __exit__
        end = time.monotonic()
        print(f"{msg} : {end - start} seconds")
        return True


# 2.1. with 문으로 리소스의 획득과 해제를 자동으로 처리합니다
with ExcuteTimerDc("Process time") as timer:
    print("Processing...")
    for i in range(1000000):  # 100만 번 반복하는 더미 작업
        pass
