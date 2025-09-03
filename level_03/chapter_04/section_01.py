# 메타클래스: 클래스 생성 과정을 제어하는 클래스

# 1. 기본 클래스와 메타클래스 이해
class SampleA():
    pass


obj1 = SampleA()  # obj1은 SampleA 클래스의 인스턴스
print(obj1.__class__)  # obj1의 클래스 정보 출력
print(type(obj1))  # 모든 클래스는 type이라는 메타클래스로 생성됨
print(obj1.__class__.__class__)  # SampleA 클래스의 메타클래스 (type) 출력
print(type.__class__)  # 체인의 끝은 type이라는 메타클래스로 더 깊은 단계는 존재하지 않음
print()


# 2. 클래스 생성 과정 이해
class SampleB():
    pass


n = 10
d = {'a': 10, 'b': 20}
obj2 = SampleB()

for o in (n, d, obj2):
    print(f"object:{o}, class:{o.__class__}, metaclass:{o.__class__.__class__}")
print("---")

for t in (int, float, dict, list, tuple, object):
    print(f"object:{t}, class:{t.__class__}, metaclass:{t.__class__.__class__}")
print()
