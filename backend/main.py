from fastapi import FastAPI

app = FastAPI(title="AI Music Video Generator API", version="1.0")

@app.get("/")
def root():
    return {"message": "Welcome to the AI Music Video Generator API"}
