# 외장(External) 함수
import os
import pickle
import random
import sys
import time
import webbrowser

# 1. sys: 시스템 관련 정보 제공

# 1.1. 명령 줄 인자
print(sys.argv)

# 1.2. 강제 종료
# sys.exit()

# 1.3. 파이썬 패키지 경로
print(sys.path)
print("---")

# 2. pickle: 파일 읽기/쓰기

# 2.1. 파일 쓰기
f = open("test.obj", "wb")
obj = {1: "python", 2: "study", 3: "basic"}
pickle.dump(obj, f)
f.close()

# 2.2. 파일 읽기
f = open("test.obj", "rb")
data = pickle.load(f)
print(data, type(data))
f.close()
print("---")

# 3. os: 운영체제 관련 정보 제공

# 3.1. 환경 변수 목록
print(os.environ["USERNAME"])
print(os.environ["CUDA_PATH"])

# 3.2. 현재 경로
print(os.getcwd())
print("---")

# 4. time: 시간 관련 정보 제공

# 4.1. 유닉스 타임스탬프
print(time.time())

# 4.2. 시간 정보 변환
print(time.localtime(time.time()))

# 4.3. 간단 표현
print(time.ctime())

# 4.4. 형식 표현
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# 4.5. 시간 간격 지정
for i in range(5):
    print(i)
    time.sleep(0.05)
print("---")

# 5. random: 랜덤 관련 정보 제공

# 5.1. 0 ~ 1 사이 랜덤 실수 생성
print(random.random())

# 5.2. 랜덤 정수 생성
print(random.randint(1, 45))
print(random.randrange(1, 45))

# 5.3. 섞기
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# 5.4. 랜덤 문자 생성
c = random.choice(d)
print(c)
print("---")

# 6. webbrowser: 웹 브라우저 관련 정보 제공

# 6.1. 웹 브라우저 실행
webbrowser.open("https://google.com")
webbrowser.open_new("https://google.com")
