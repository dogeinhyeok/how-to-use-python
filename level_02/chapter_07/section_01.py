from collections import abc

# 병행성(Concurrency): 동시 실행
# Iterator, Generator

# 1. 반복 가능한 이유? -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in t:
    print(c)
print()

# 1.1. for문 내부적으로 자동으로 iter(x) 함수 호출
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

# 2. 반복형 확인
print(hasattr(t, '__iter__'))  # __iter__ 메서드가 있는지 확인
print(isinstance(t, abc.Iterable))  # Iterable을 상속 받았는지 확인
print()


# 3. next 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print()


# 4. Generator 패턴
class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)


wg = WordSplitGenerator('Do today what you could do tomorrow')
print(wg)
wt = iter(wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print()
