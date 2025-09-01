import time


# 실행 시간을 측정하는 Context Manager 클래스
class ExcuteTimer(object):
    def __init__(self, msg):
        self.msg = msg  # 출력할 메시지 저장

    def __enter__(self):
        self.start = time.time()  # 시작 시간 기록
        return self  # 자기 자신을 반환하여 with 블록에서 사용 가능

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            # 예외가 발생한 경우 예외 정보 출력
            print(f"Logging exception {exc_value}, {exc_type}, {traceback}")
        else:
            # 정상 종료인 경우 실행 시간 계산 및 출력
            self.end = time.time()
            print(f"{self.msg} : {self.end - self.start} seconds")
        return True  # 예외를 억제함


# Context Manager를 사용하여 실행 시간 측정
with ExcuteTimer("Process time") as timer:
    print("Processing...")
    for i in range(1000000):  # 100만 번 반복하는 더미 작업
        pass
