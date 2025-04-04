# 사용자 입력

# 1. 기본 타입(str)
name = input("Enter Your Name: ")
grade = input("Enter Your Grade: ")
company = input("Enter Your Company: ")
print(f"name: {name}, grade: {grade}, company: {company}")

# 2. 변환 타입
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
total = first_num + second_num
print(f"first_num + second_num = {total}")

# 3. 입력과 동시에 출력
print(f"FirstName: {input('Enter FirstName: ')}, LastName: {input('Enter LastName: ')}")
