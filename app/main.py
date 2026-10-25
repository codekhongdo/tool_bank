from fastapi import FastAPI
from app.api.webhooks.sepay import router
app = FastAPI(title="Tool Bank")
app.include_router(router)
@app.get("/health")
def health():
    return {"status": "ok"}
