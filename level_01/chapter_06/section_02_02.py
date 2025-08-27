# 사용자 입력 예외 처리

# 1. 예외 처리 기본
try:
    n = int(input("Enter a number:"))
    print(f"OK. Your number is {n}")
except ValueError:
    print("This is not a number.")
print()

# 2. 예외 처리 반복
while True:
    try:
        n = int(input("Enter a number: "))
        print(f"OK. Your number is {n}")
        break
    except ValueError:
        print("This is not a number.")
print()
