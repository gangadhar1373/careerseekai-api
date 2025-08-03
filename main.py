from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the CareerSeekAI backend!"}

handler = Mangum(app)