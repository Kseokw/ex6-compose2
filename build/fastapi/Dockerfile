# 1. 기본 이미지 설정
FROM python:3.9-slim

# 2. 작업 디렉토리 정의
WORKDIR /app

# 환경변수 설정
# PYTHONDONTWRITEBYTECODE: 파이썬이 .pyc 파일을 생성하지 않도록 설정
# PYTHONUNBUFFERED: 파이썬 출력 버퍼링을 비활성화하여 로그를 실시간으로 확인 가능하도록 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# 3. requirements.txt 파일을 컨테이너로 복사
# 복사 위치는 위에 정의한 작업 디렉토리
COPY requirements.txt .

# 4. requirements.txt 파일에 정의된 패키지(라이브러리) 설치
# --no-cache-dir: 설치 후 캐시를 남기지 않도록 하는 옵션
RUN pip install --no-cache-dir -r requirements.txt

# 5. 현재 디렉토리의 모든 파일을 이미지로 복사
# 현재 디렉토리(fastapi/app/) -> 컨테이너 내부의 작업 디렉토리(/app)로 복사
COPY ./app/ .

# 6. 컨테이너 내부 포트 보여주기
EXPOSE 8000

# 7. 컨테이너 실행 시 실행할 명령 구성
# "--reload": 운영환경에서는 포함하지 않습니다.(개발환경에서만 사용)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# docker run 예시
# CMD만 사용 시
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# docker run -d -p 9000:9000 --name my-app my-fastapi-v1 uvicorn main:app --host 0.0.0.0 --port 9000
# ENTRYPOINT와 CMD를 함께 사용 시
# ENTRYPOINT ["uvicorn"]
# CMD ["main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# docker run -d -p 9000:9000 --name my-app my-fastapi-v1 --port 9000

