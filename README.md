# 파이썬 학습 프로젝트

이 프로젝트는 파이썬 학습을 위한 통합 문서화 프로젝트로, 초보자부터 상급자까지 모두가 쉽게 배울 수 있는 환경을 제공합니다.

## 설치 및 설정

### 1. 가상환경 생성

```bash
python -m venv venv
```

### 2. 가상환경 활성화

#### Windows (PowerShell)

```bash
.\venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)

```bash
.\venv\Scripts\activate.bat
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

## 프로젝트 구조

```
level_01/          # 초급 레벨
├── chapter_03/    # 기본 문법
├── chapter_04/    # 자료형
├── chapter_05/    # 제어문
├── chapter_06/    # 함수
├── chapter_07/    # 모듈과 패키지
├── chapter_08/    # 예외처리
├── chapter_09/    # 내장함수
└── chapter_10/    # 파일 입출력

level_02/          # 중급 레벨
├── chapter_03/    # 고급 문법
├── chapter_04/    # 클래스와 객체
├── chapter_05/    # 상속과 다형성
├── chapter_06/    # 데코레이터
└── chapter_07/    # 비동기 프로그래밍

level_03/          # 고급 레벨 (준비 중)
level_04/          # 전문 레벨 (준비 중)
```

## 사용 방법

1. 가상환경을 활성화합니다
2. 원하는 챕터의 파이썬 파일을 실행합니다
3. 예: `python level_01/chapter_03/section_01_01.py`

## 가상환경 비활성화

작업이 끝나면 가상환경을 비활성화합니다:

```bash
deactivate
```
