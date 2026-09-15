#!/bin/bash

# 1. 컴포즈 작업 폴더 생성
mkdir -p /home/ec2-user/nginx/html
mkdir -p /home/ec2-user/nginx/logs

mkdir -p /home/ec2-user/fastapi/app
mkdir -p /home/ec2-user/fastapi/logs

# 4. 소유권 변경
chown -R ec2-user:ec2-user /home/ec2-user/nginx
chown -R ec2-user:ec2-user /home/ec2-user/fastapi


# 3. S3에서 index.html 과 docker-compose.yaml 다운로드
cd /home/ec2-user/nginx
aws s3 cp s3://std07-git-web-s3/index.html /home/ec2-user/nginx/html/index.html
aws s3 cp s3://std07-git-web-s3/web-compose/docker_compose_nginx.yaml .

cd /home/ec2-user/fastapi
aws s3 cp s3://std07-git-web-s3/web-compose/docker_compose_fastapi.yaml .



# 5. ECR 로그인 및 컨테이너 실행
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 925047940866.dkr.ecr.ap-southeast-1.amazonaws.com
docker compose pull
docker compose up -d