from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import divination_router, health_router

app = FastAPI(
    title="千机后端",
    description="人生推演系统后端 API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(divination_router, prefix="/api/v1")
app.include_router(health_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "千机后端服务运行中", "docs": "/docs"}
