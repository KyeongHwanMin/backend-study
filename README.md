# 원티드 프리 온보딩 백엔드 과제 - 민경환

## pre requirements
- Pyenv(https://github.com/pyenv/pyenv)

## 프로젝트 스펙 정보
- Python 3.11.x
- Django 4.0.x
- djangorestframework 3.14.x

## 개발 환경 세팅
```bash
# python 설치
pyenv install 3.11.6
# 가상환경 설치
pyenv virtualenv 3.11.6 3.11.6_wanted_pre_onboarding_backend
# 가상환경 경로 진입시 자동 활성화 설정
pyenv local 3.11.6_wanted_pre_onboarding_backend .
# 가상환경 활성화
pyenv version 3.11.6_wanted_pre_onboarding_backend
# 의존성 설치
pip install -r requirements.txt
# 데이터베이스 마이그레이션
python manage.py migrate
```

## 서버 정상 실행 확인
```bash
python manage.py runserver
```
위 명령 실행 결과로 아래와 같은 콘솔 출력이 뜨고, http://127.0.0.1:8000/ 접속이 되면 정상이다.
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2023 - 13:40:31
Django version 4.0.10, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
