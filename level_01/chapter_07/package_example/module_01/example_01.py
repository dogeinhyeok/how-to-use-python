import inspect


def mod1_func1():
    print("func: mod1_func1")
    print(f"path: {inspect.getfile(inspect.currentframe())}")


def mod1_func2():
    print("func: mod1_func2")
    print(f"path: {inspect.getfile(inspect.currentframe())}")
