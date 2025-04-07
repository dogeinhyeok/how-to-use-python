# 변수 사용법

# 1. 기본 선언
n = 700

# 2. 출력
print(n)
print(type(n))
print()

# 3. 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 4. 선언
var = 75

# 5. 재선언
var = "Change Value"

# 6. 출력
print(var)
print(type(var))
print()

# 7. Object Reference
"""
> 변수 값 할당 상태
> 1. 타입에 맞는 오브젝트 생성
> 2. 값 생성
> 3. 콘솔 출력
"""

# 7.1. 예제 1
print(300)
print(int(300))
print()

# 7.2. 예제 2
n = 777
print(n, type(n))
print()

m = n
print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# 8. id(identity) 주소값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 8.1. 파이썬 인터프리터에서 동일한 값을 가진 변수는 같은 주소값을 공유
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 9. 다양한 변수 선언
"""
> Pascal Case: NumberOfCollegeGraduates -> Class
> Snake Case: number_of_college_graduates -> Variable, Function, File, Folder
> Kebab Case: number-of-college-graduates -> URL, HTML, CSS
> + 예약어는 변수명으로 사용 불가
"""
