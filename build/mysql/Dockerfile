FROM mysql:8.0

# 컨테이너의 /docker-entrypoint-initdb.d 디렉토리에 있는 모든 .sql 파일을 실행하여
# 데이터베이스를 초기화 할 때 사용한다.
COPY ./init_onlydb.sql /docker-entrypoint-initdb.d/
COPY ./my.cnf /etc/mysql/conf.d/my.cnf

ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE=testdb
ENV MYSQL_USER=std07
ENV MYSQL_PASSWORD=1234
# root의 비밀번호를 난수로 지정
# ENV MYSQL_RANDOM_ROOT_PASSWORD=yes
# CMD는 사용하지 않습니다. 기본 이미지에서 이미 CMD를 설정하고 있기 때문에, CMD를 설정하면 기존 CMD가 무시됩니다.