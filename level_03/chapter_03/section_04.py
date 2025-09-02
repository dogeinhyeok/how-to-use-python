import datetime

# 상속


# 1. Overriding 기본 예제
class ParentEx1():
    def __init__(self):
        self.value = 100

    def get_value(self):
        return self.value


class ChildEx1(ParentEx1):
    pass


c1 = ChildEx1()
p1 = ParentEx1()


# 1.1. 부모클래스 메소드 호출
print(f"c1.get_value(): {c1.get_value()}")  
print()


# 2. 기본 Overriding 메소드 재정의
class ParentEx2():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10


# 2.1. 재정의된 메소드 호출
c2 = ChildEx2()
print(f"c2.get_value(): {c2.get_value()}")  
print()


# 3. Overriding 다형성 예제
class Logger(object):
    def log(self, message):
        print(message)


class TimeStampLogger(Logger):
    def log(self, message):
        timestamped_message = f"{datetime.datetime.now()}: {message}"
        super().log(timestamped_message)


class DateLogger(Logger):
    def log(self, message):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        dated_message = f"{current_date}: {message}"
        super().log(dated_message)


logger = Logger()
timestamp_logger = TimeStampLogger()
date_logger = DateLogger()

logger.log("Hello, World!")
timestamp_logger.log("Hello, World!")
date_logger.log("Hello, World!")
print()
