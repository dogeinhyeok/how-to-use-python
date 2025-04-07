# while 구문
"""
> while <조건>:
>     <실행문>
"""

# 1. 예제 1
n = 5
while n > 0:
    print(n)
    n = n - 1
print()

# 2. 예제 2
a = ["foo", "bar", "baz"]
while a:
    print(a.pop())
print()

# 3. 예제 3
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print()

# 4. 예제 4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print()

# 5. 예제 5
i = 1
while i <= 10:
    print("i:", i)
    if i == 6:
        break
    i += 1
print()

# 6. While - else 구문
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print("else out")
print()

# 6.1. 예제
a = ["foo", "bar", "baz", "qux"]
s = "kim"
i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, "not found in list.")
print()

# 7. 무한반복
"""
> while True:
>     <실행문>
"""

# 7.1. 예제
a = ["foo", "bar", "baz"]
while True:
    if not a:
        break
    print(a.pop())
