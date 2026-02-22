"""cognitive-link-processor-realtime-twp - AI Infrastructure Component"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"service": "cognitive-link-processor-realtime-twp", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
