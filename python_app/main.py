from fastapi import FastAPI
from python_app.api.search_api import router as search_router
from python_app.api.assistant_api import router as assistant_router

app = FastAPI(
    title="Library AI Service",
    description="AI/ML service for Library Management System",
    version="1.0.0",
)


app.include_router(search_router)
app.include_router(assistant_router)


@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "library-ai-service"
    }