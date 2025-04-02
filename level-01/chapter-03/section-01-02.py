# 3가지 Format 사용법

x = 50
y = 100
text = 308276567
n = "Lee"

# 1. 기본 출력 예제
ex1 = "n = %s, s = %s, sum = %d" % (n, text, (x + y))
print(ex1)
print()

# 2. format 옵션 예제
ex2 = "n = {n}, s = {s}, sum = {sum}".format(n=n, s=text, sum=x + y)
print(ex2)
print()

# 3. f-string 사용 예제
ex3 = f"n = {n}, s = {text}, sum = {x + y}"
print(ex3)
print()

# 4. 구분기호
m = 100000000
print(f"m : {m:,}")
print()

# 6. 정렬
"""
> ^ : 가운데 정렬
> < : 왼쪽 정렬
> > : 오른쪽 정렬
"""
t = 20
print(f"t : {t:20}")
print(f"t : {t:^20}")
print(f"t : {t:<20}")
print(f"t : {t:>20}")
print(f"t : {t:-^20}")
print(f"t : {t:#^20}")
print()
