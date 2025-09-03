# Descriptor: "속성을 읽고, 쓰고, 삭제할 때 커스터마이징하는 기능
# @property는 내부적으로 Descriptor로 구현되었습니다.

# 1. 기본적인 Descriptor 예제
class DescriptorA(object):
    def __init__(self, value="default"):
        self.value = value

    def __get__(self, instance, instance_type):
        return ("Get method called. -> ",
                f"self: {self}, "
                f"instance: {instance}, "
                f"instance_type: {instance_type}, "
                f"value: {self.value}")

    def __set__(self, instance, value):
        print("Set method called.")
        if isinstance(value, str):
            self.value = value
        else:
            raise TypeError("Name must be a string.")

    def __delete__(self, instance):
        print("Delete method called.")
        self.name = None


class SampleA(object):
    value = DescriptorA()


s1 = SampleA()

s1.value = "Descriptor Test A"  # __set__ 호출
print(s1.value)  # __get__ 호출
del s1.value  # __delete__ 호출
print(s1.value)  # __get__ 호출
print()


# 2. Property 클래스 사용 Descriptor 직접 구현
class DescriptorB(object):
    def __init__(self, value="default"):
        self._value = value

    def getValue(self):
        return f"Get method called. -> value: {self}, name: {self._value}"

    def setValue(self, value):
        print("Set method called.")
        if isinstance(value, str):
            self._value = value
        else:
            raise TypeError("Value must be a string.")

    def deleteValue(self):
        print("Delete method called.")
        self._value = None

    value = property(getValue, setValue, deleteValue, "Property Method Example")


s2 = DescriptorB("Descriptor Test B")

s2.value = "Descriptor Test B"
print(s2.value)
del s2.value
print()
