from fastapi import FastAPI

app = FastAPI(
    title="Modern Fraud Detection - FastAPI",
    description="A modern fraud detection system built with FastAPI.",
)

@app.get("/")
def home():
    return {"message": "Welcome to the Modern Fraud Detection API!"}