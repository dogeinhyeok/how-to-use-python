import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# AsyncIO 멀티 스크래핑: 여러 웹사이트를 동시에 데이터를 수집하는 기술

# 실행 시작 시간
start = timeit.default_timer()

# 수집할 웹사이트 URL 목록
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://www.inflearn.com/']


# 각 URL에서 제목(title) 추출하는 함수
async def fetch(url, executor, loop):
    # 쓰레드명 출력(시작)
    print('Thread Name :', threading.current_thread().name, 'Start', url)
    # 실행
    response = await loop.run_in_executor(executor, urlopen, url)
    # 쓰레드명 출력(완료)
    print('Thread Name :', threading.current_thread().name, 'Done', url)
    # 결과 반환
    return response.read()[0:5]


async def main():
    # 쓰레드 풀 생성 (10개 쓰레드)
    executor = ThreadPoolExecutor(max_workers=10)

    # 현재 이벤트 루프 가져오기
    loop = asyncio.get_running_loop()

    # 각 URL마다 fetch() 함수를 Future 객체로 변환
    futures = [
        # ensure_future()는 코루틴을 Future 객체로 변환
        asyncio.ensure_future(fetch(url, executor, loop)) for url in urls
    ]

    # gather()에서 모든 Future 객체들을 동시에 실행
    result = await asyncio.gather(*futures)
    print()

    # 모든 Future 객체들의 결과를 출력
    print('Result : ', result)
    print()

    # 쓰레드 풀 종료
    executor.shutdown()

if __name__ == '__main__':
    # 작업 완료 까지 대기
    asyncio.run(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)
    print()
