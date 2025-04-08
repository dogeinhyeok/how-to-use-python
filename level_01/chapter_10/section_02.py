# 파일 읽기 및 쓰기(csv)

import csv
import os

# 1. 현재 파일의 절대 경로를 기준으로 상대 경로 계산
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "test1.csv")

# 2. 파일 기본 정보 읽기
with open(file_path, "r") as f:
    reader = csv.reader(f)
    print(reader)  # 객체 확인
    print(type(reader))  # 타입 확인
    print(dir(reader))  # 속성 확인
    for c in reader:
        print(c)
print("---")

# 2. 파일 기본 정보 읽기
file_path = os.path.join(current_dir, "test2.csv")
with open(file_path, "r") as f:
    reader = csv.reader(f, delimiter="|")
    for c in reader:
        print(c)
print("---")

# 3. 파일 딕셔너리 형식 읽기
file_path = os.path.join(current_dir, "test1.csv")
with open(file_path, "r") as f:
    reader = csv.DictReader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))
    for c in reader:
        for k, v in c.items():
            print(f"{k}: {v}")
print("---")

# 4. 파일 쓰기
file_path = os.path.join(current_dir, "write1.csv")
w = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
]

# 4.1. 파일 리스트 형식 쓰기
with open(file_path, "w", encoding="utf-8") as f:
    print(dir(csv))
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)

# 4.2. 파일 딕셔너리 형식 쓰기
file_path = os.path.join(current_dir, "write2.csv")
with open(file_path, "w", encoding="utf-8") as f:
    fields = ["One", "Two", "Three"]  # CSV 파일의 컬럼 이름을 정의
    wt = csv.DictWriter(f, fieldnames=fields)  # 컬럼 이름을 지정하여 CSV 작성기 생성
    wt.writeheader()  # 컬럼 이름을 파일의 첫 줄에 작성
    for v in w:
        row_dict = {"One": v[0], "Two": v[1], "Three": v[2]}  # 딕셔너리 형태로 변환
        wt.writerow(row_dict)
