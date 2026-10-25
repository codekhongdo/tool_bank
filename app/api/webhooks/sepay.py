from fastapi import APIRouter, Request, Header, Depends, HTTPException
import secrets
from app.core.config import get_settings
from app.services.parser import parse_transfer
from app.services.excel_exporter import ExcelExporter
router = APIRouter()

def require_token(authorization: str | None = Header(None)):
    settings = get_settings()
    expected_token = settings.SEPAY_WEBHOOK_AUTH_TOKEN
    if not authorization:
        raise HTTPException(status_code=401, detail="Thiếu header Authorization")
    parts = authorization.split()
    if len(parts) != 2:
        raise HTTPException(status_code=401, detail="Sai định dạng Authorization")
    scheme, token = parts[0], parts[1]
    if scheme.lower() not in ("bearer", "apikey"):
        raise HTTPException(status_code=401, detail="Scheme không được hỗ trợ")
    if not secrets.compare_digest(token, expected_token):
        raise HTTPException(status_code=401, detail="Token không chính xác")
    return True
@router.post("/api/webhooks/sepay")
async def sepay_webhook(
    request: Request,
    _auth: bool = Depends(require_token),
):
    body = await request.json()
    content = body.get("content", "")
    amount = body.get("transferAmount", 0)
    transaction_date = body.get("transactionDate", "")
    transaction_id = body.get("id", "")
    payment = parse_transfer(
    content=content,
    soTien=amount,
    thoiGian=transaction_date,
    transactionId=transaction_id,
   )
    if payment is None:
        return {"success": True, "status": "ignored"}
    exporter = ExcelExporter()
    appended = exporter.append(payment)

    if appended:
        return {"success": True, "status": "ok"}
    return {"success": True, "status": "duplicate"}
