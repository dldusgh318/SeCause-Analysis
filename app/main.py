from fastapi import FastAPI
from app.api.routes import analyze
from app.core.database import init_db

app = FastAPI(title="SeCause Analysis Server")

# Startup event
@app.on_event("startup")
async def startup():
    await init_db()

# Include routers
app.include_router(analyze.router, prefix="/api", tags=["analyze"])

# Internal routes
@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)