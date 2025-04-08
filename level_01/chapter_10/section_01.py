# 파일 읽기 및 쓰기(txt)
"""
> 읽기 모드: r
> 쓰기 모드: w
> 추가 모드: a
> 텍스트 모드: t
> 바이너리 모드: b
"""

import os

# 1. 현재 파일의 절대 경로를 기준으로 상대 경로 계산
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "it_news.txt")

# 2. 파일 기본 정보 출력
f = open(file_path, "r", encoding="UTF-8")  # 파일 읽기
print("dir(f):", dir(f))  # 속성 확인
print("file encoding:", f.encoding)  # 인코딩 확인
print("file path:", f.name)  # 파일 경로
print("file mode:", f.mode)  # 모드 확인
cts = f.read()  # 파일 내용 전체 읽기
print("file contents:", cts)
f.close()  # 파일 닫기
print("---")

# 3. 파일 전체 읽기
with open(file_path, "r", encoding="UTF-8") as f:
    cts = f.read()
    print("file contents:", cts)
    print(iter(cts))
    print(list(cts))
print("---")

# 4. 한 글자씩 읽기
with open(file_path, "r", encoding="UTF-8") as f:
    cts = f.read(2)
    print("file contents:", cts)
    cts = f.read(3)
    print("file contents:", cts)
    cts = f.read(1)
    print("file contents:", cts)
print("---")

# 5. 한 줄씩 읽기
with open(file_path, "r", encoding="UTF-8") as f:
    line = f.readline()
    print("line:", line, end="")
    line = f.readline()
    print("line:", line)
print("---")

# 6. 전체를 읽기 후 한 줄씩 쓰기
with open(file_path, "r", encoding="UTF-8") as f:
    cts = f.readlines()
    print(cts)
    for c in cts:
        print(c, end="")
    print()
print("---")

# 7. 파일 쓰기
file_path = os.path.join(current_dir, "contents1.txt")
with open(file_path, "w", encoding="UTF-8") as f:
    f.write("I love Python\n")

# 8. 파일 추가
file_path = os.path.join(current_dir, "contents1.txt")
with open(file_path, "a", encoding="UTF-8") as f:
    f.write("Python is awesome\n")

# 9. 리스트 -> 파일
file_path = os.path.join(current_dir, "contents2.txt")
with open(file_path, "w", encoding="UTF-8") as f:
    list = [
        "Orange\n",
        "Apple\n",
        "Banana\n",
        "Melon\n",
    ]
    f.writelines(list)

# 10. 파일 출력
file_path = os.path.join(current_dir, "contents3.txt")
with open(file_path, "w", encoding="UTF-8") as f:
    print("Test Text Write!", file=f)
    print("Test Text Write!", file=f)
    print("Test Text Write!", file=f)
