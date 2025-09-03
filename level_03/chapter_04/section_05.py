import os
import logging

# Descriptor 심화


# 1. Descriptor 예제 1
class DirectoryFileCount:
    def __get__(self, instance, instance_type=None):
        print(os.listdir(instance.dirname))
        return len(os.listdir(instance.dirname))


class DirectoryPath:
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname


# 현재 경로
s = DirectoryPath("./")

print(s.size)
print()

# 2. Descriptor 예제 2
logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)


class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, instance, instance_type=None):
        logging.info(f"Accessing score giving {self.value}")
        return self.value

    def __set__(self, instance, value):
        logging.info(f"Updating score to {value}")
        self.value = value

    def __delete__(self, instance):
        logging.info("Deleting score")
        self.value = None


class Student:
    # Descriptor 인스턴스 메소드
    score = LoggedScoreAccess()  # 클래스 변수

    def __init__(self, name):
        self.name = name


s1 = Student("John")
s2 = Student("Jane")

s1.score += 20
s2.score += 30  # 클래스 변수라 점수 공유됨

print()
