import time
from concurrent import futures
"""
> ProcessPoolExecutor: 각 프로세스가 별도 CPU 코어에서 실행되므로 CPU-bound 작업에 효과적
> ThreadPoolExecutor: 빠르게 번갈아가며 쓰레드를 사용하여 I/O 대기 시간에
>                     다른 쓰레드를 실행할 수 있어 I/O-bound 작업에 효과적
"""


# 4개의 큰 숫자들의 누적 합계를 계산
WORK_LIST = [10000, 100000, 1000000, 10000000]


# 1부터 n까지의 합계를 계산
def sum_generator(n):
    return sum(n for n in range(1, n+1))


def main():
    # 시작 시간
    start_tm = time.time()

    # 결과 리스트
    result = []

    # 멀티스레딩 처리
    with futures.ThreadPoolExecutor() as executor:  # 스레드 풀 생성
        result = executor.map(sum_generator, WORK_LIST)  # 함수를 여러 인자에 대해 동시에 실행

    # 종료 시간
    end_tm = time.time()

    # 최종 결과 촐력
    msg = '\n Result -> {} Time : {:.2f}s'
    print(msg.format(list(result), end_tm - start_tm))


# 실행
if __name__ == "__main__":
    main()
