# 1. 기본 이미지 설정
FROM nginx:1.31.3-alpine

# 2. 기본 이미지의 default.conf 파일을 삭제
# RUN: 컨테이너(기본 이미지) 내부 명령
RUN rm /etc/nginx/conf.d/default.conf

# 3. 사용자의 파일로 기본 이미지의 default.conf 파일을 대체
# COPY: 컨테이너(기본 이미지) 내부로 파일 복사
COPY ./default.conf /etc/nginx/conf.d/default.conf

# 4. HTML 내의 파일 및 디렉토리를 컨테이너로 복사
COPY ./html/ /usr/share/nginx/html/

# 5. 컨테이너 내부 포트 보여주기
EXPOSE 80

# 6. 컨테이너 실행 시 실행할 명령 구성
CMD ["nginx", "-g", "daemon off;"]

