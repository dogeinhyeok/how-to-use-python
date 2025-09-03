# 1. 커스텀 메타클래스 생성 예제
def custom_multiple(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d


def custom_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


CustomList1 = type("CustomList1", (list,), {
    "multiple": custom_multiple,
    "replace": custom_replace
})  # CustomListMeta과 같은 기능의 함수

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9])
c1.multiple(10)
c1.replace(10, "a")
print(c1)
print(CustomList1.__mro__)
print()


# 2. 커스텀 상속 메타클래스 생성 예제
class CustomListMeta(type):
    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print("__init__", self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)

    # 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print("__call__", self, *args, **kwargs)
        return super().__call__(*args, **kwargs)

    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__(cls, name, bases, dict):
        print("__new__", cls, name, bases, dict)
        dict["multiple"] = custom_multiple
        dict["replace"] = custom_replace
        return type.__new__(cls, name, bases, dict)


CustomList2 = CustomListMeta("CustomList2", (list,), {})
c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2.multiple(10)
c2.replace(10, "a")
print(c2)
print(CustomList2.__mro__)
print()
