# 파이썬 패키지

# 1. 패키지의 모듈을 별칭(alias)으로 임포트
import package_example.module_01.example_01 as example_01
import package_example.module_02.example_02 as example_02

# 2. 특정 모듈에서 특정 함수만 임포트
from package_example.module_01.example_01 import mod1_func1, mod1_func2
from package_example.module_02.example_02 import mod2_func1, mod2_func2

# 3. 임포트한 함수 직접 사용
mod1_func1()
mod1_func2()
mod2_func1()
mod2_func2()
print("---")

# 4. 모듈 이름을 통한 함수 사용
example_01.mod1_func1()
example_02.mod2_func1()
