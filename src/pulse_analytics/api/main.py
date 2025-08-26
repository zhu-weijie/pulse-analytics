from fastapi import FastAPI

app = FastAPI(
    title="Pulse Analytics API",
    description="API for managing and triggering data processing jobs.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pulse Analytics API"}


@app.get("/health")
def read_health():
    return {"status": "ok"}
