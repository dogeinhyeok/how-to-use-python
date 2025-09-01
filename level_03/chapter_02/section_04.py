import os

# 프로젝트 루트 디렉토리 찾기
current_file = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
testfile1 = os.path.join(project_root, 'output', 'testfile1.txt')
testfile2 = os.path.join(project_root, 'output', 'testfile2.txt')
testfile3 = os.path.join(project_root, 'output', 'testfile3.txt')
testfile4 = os.path.join(project_root, 'output', 'testfile4.txt')

# 예제 1
file = open(testfile1, 'w')
try:
    file.write('Context Manager Test1\nContext Manager Test2')
finally:
    file.close()

# 예제 2
with open(testfile2, 'w') as file:
    file.write('Context Manager Test3\nContext Manager Test4')


# 예제 3
class MyFileWriter:
    def __init__(self, file_path, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_path, method)

    # with 문이 시작될 때 호출되어 사용할 객체를 반환함
    def __enter__(self):
        print("MyFileWriter started : __enter__")
        return self.file_obj

    def __exit__(self, exc_type, exc_value, traceback):
        print("MyFileWriter started : __exit__")
        if exc_type:
            print(f"Logging exception {exc_value}, {exc_type}, {traceback}")
        self.file_obj.close()


# with 구문은 파일, 네트워크 연결, 데이터베이스 연결 등을 사용한 후 자동으로 해제합니다
# __enter__가 반환하는 객체가 as 뒤의 변수에 할당됩니다
with MyFileWriter(testfile3, 'w') as file:
    file.write('Context Manager Test5\nContext Manager Test6')
