# SeCause-Analysis

## 🚀 로컬 개발 시작

### 1. 저장소 클론
```bash
git clone https://github.com/SeCause/SeCause-Analysis.git
cd SeCause-Analysis
```

### 2. 가상환경 생성 및 활성화
```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 환경변수 설정
```bash
cp .env.example .env
```

`.env` 에 노션에 있는 값 넣기

### 5. 서버 실행
```bash
python -m uvicorn app.main:app --reload --port 8001
```

### 6. 확인
- API 문서: http://localhost:8001/docs
- 헬스 체크: http://localhost:8001/health