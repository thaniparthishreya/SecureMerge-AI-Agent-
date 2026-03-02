from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def gitlab_webhook(request: Request):
    data = await request.json()
    print("Received event:", data.get("object_kind"))
    return {"status": "received"}