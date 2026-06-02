from fastapi import FastAPI
from app.api.routes import analyze
from contextlib import asynccontextmanager
from app.core.database import init_db, engine
from app.core.config import settings
import logging
 
# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Startup event
@asynccontextmanager
async def lifespan(app: FastAPI):
        # ===== Startup =====
    logger.info("🚀 FastAPI Server Starting...")
    try:
        await init_db()
        logger.info("✅ Database connection initialized")
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        raise
    
    yield
    
    # ===== Shutdown =====
    logger.info("🛑 FastAPI Server Shutting down...")
    try:
        # DB 엔진 정리
        await engine.dispose()
        logger.info("✅ Database connections closed")
    except Exception as e:
        logger.error(f"❌ Error during shutdown: {e}")

 
# FastAPI 앱 생성
app = FastAPI(
    title="SeCause Analysis Server",
    description="Security Analysis Pipeline for SeCause",
    version="0.1.0",
    lifespan=lifespan,
)

# 라우터 등록
app.include_router(analyze.router, prefix="/api", tags=["analyze"])
 
 
# Health Check 엔드포인트
@app.get("/health", tags=["health"])
async def health_check():
    """
    서버 헬스 체크
    """
    return {
        "status": "ok",
        "service": "SeCause Analysis Server",
        "version": "0.1.0"
    }
 
 
# Root 엔드포인트
@app.get("/", tags=["root"])
async def root():
    """
    루트 경로
    """
    return {
        "message": "SeCause Analysis Server",
        "docs": "/docs",
        "health": "/health"
    }
 
 
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info",
    )