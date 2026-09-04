from fastapi import FastAPI

app = FastAPI(
    title="Library AI Service",
    description="AI/ML service for Library Management System",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "library-ai-service"
    }