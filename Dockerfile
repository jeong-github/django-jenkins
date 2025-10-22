# Python 3.8 이미지를 사용하여 호환성 문제를 해결
FROM python:3.8-slim

# 환경 변수 설정
ENV PYTHONUNBUFFERED 1

# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 최신 pip, setuptools, wheel 설치
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 작업 디렉토리 설정
WORKDIR /code

# 요구사항 파일 복사 및 설치
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY chanDjango /code/


# 서버 실행
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
