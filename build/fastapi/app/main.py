from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pymysql
import os

# app을 선언할 때 root_path 지정
# app = FastAPI(root_path="/board")
app = FastAPI()

# templates 폴더 설정 (index.html이 있는 위치)
templates = Jinja2Templates(directory="templates")

# MySQL 연결 설정 (본인 환경에 맞게 수정하세요)
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": 3306,
    "charset": "utf8mb4"
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # 페이지에 표시될 데이터 정의
    k8s_data = {
        "title": "Kubernetes Navigation",
        "subtitle": "컨테이너 오케스트레이션의 바다를 항해하다",
        "sections": [
            {"id": "arch", "title": "Cluster Architecture", "desc": "Control Plane & Worker Node"},
            {"id": "object", "title": "K8s Objects", "desc": "Pod, Service, Deployment"},
            {"id": "network", "title": "Networking", "desc": "Ingress & Service Mesh"},
            {"id": "storage", "title": "Storage & PV", "desc": "Persistent Volumes"}
        ]
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": k8s_data})

@app.get("/db-check")
def check_db_connection():
    try:
        # 데이터베이스 연결 시도
        connection = pymysql.connect(**DB_CONFIG)

        # 연결이 성공하면 정상적으로 닫아줌
        connection.close()

        return {"status": "connected"}

    except Exception as e:
        # 연결 실패 시 에러 내용 반환
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
