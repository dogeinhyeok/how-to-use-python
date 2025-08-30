import time
from concurrent.futures import ThreadPoolExecutor, wait

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
        futures_result = wait(futures_result, timeout=7)
        print()
        print("Completed Task:", str(futures_result.done))
        print("Pending ones after waiting for 7 seconds:",
              str(futures_result.not_done))
        print([future.result() for future in futures_result.done])

    # 종료 시간
    end_tm = time.time()

    # 최종 결과 촐력
    msg = '\nTime : {:.2f}s'
    print(msg.format(end_tm - start_tm))


# 실행
if __name__ == "__main__":
    main()
