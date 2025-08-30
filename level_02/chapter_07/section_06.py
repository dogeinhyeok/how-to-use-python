import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 4개의 큰 숫자들의 누적 합계를 계산
WORK_LIST = [10000, 100000, 1000000, 10000000]


# 1부터 n까지의 합계를 계산
def sum_generator(n):
    return sum(n for n in range(1, n+1))


def main():
    # 시작 시간
    start_tm = time.time()

    # 결과 리스트
    futures_result = []

    # 멀티스레딩 처리
    with ThreadPoolExecutor() as executor:  # 스레드 풀 생성
        for work in WORK_LIST:
            future = executor.submit(sum_generator, work)
            futures_result.append(future)
            print("Scheduled for {} : {}".format(work, future))

        # as_completed 반환값 순서대로 처리
        for future in as_completed(futures_result):
            result = future.result()
            done = future.done()
            canceled = future.cancelled()

            # future 결과 확인
            print("Future Result: {}, Done : {}".format(result, done))
            print("Future Cancelled: {}".format(canceled))

    # 종료 시간
    end_tm = time.time()

    # 최종 결과 촐력
    msg = '\nTime : {:.2f}s'
    print(msg.format(end_tm - start_tm))


# 실행
if __name__ == "__main__":
    main()
