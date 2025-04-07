import inspect


def mod2_func1():
    print("func: mod2_func1")
    print(f"path: {inspect.getfile(inspect.currentframe())}")


def mod2_func2():
    print("func: mod2_func2")
    print(f"path: {inspect.getfile(inspect.currentframe())}")
