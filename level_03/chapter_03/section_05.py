from multipledispatch import dispatch

# 메소드 오버로딩


# 1. 동일 이름 메소드 사용 예제
class SampleA:
    def add(self, x, y, *args):
        return x + y + sum(args)

    # Python에서 메소드 오버로딩 지원하지 않음
    #  def add(self, x, y, z):
    #    return x + y + z


a = SampleA()
print(a.add(1, 2))
print(a.add(1, 2, 3))
print(a.add(1, 2, 3, 4))
print()


# 2. 동일 이름 메소드 사용 분기처리 예제
class SampleB:
    def add(self, datatype, *args):
        if datatype == "int":
            return sum(args)
        if datatype == "str":
            return "".join([x for x in args])


b = SampleB()
print(b.add("int", 1, 2))
print(b.add("str", "a", "b", "c"))
print()


# 3. multipledispatch 패키지를 통한 메소드 오버로딩
class SampleC:
    @dispatch(int, int)
    def add(self, x, y):
        return x + y

    @dispatch(int, int, int)
    def add(self, x, y, z):  # noqa
        return x + y + z
    
    @dispatch(float, float, float)
    def add(self, x, y, z):  # noqa
        return x + y + z


c = SampleC()
print(c.add(1, 2))
print(c.add(1, 2, 3))
print(c.add(1.0, 2.0, 3.0))
print()
