# TODO cho bạn tự code: POST /api/webhooks/sepay
# Gợi ý:
# - APIRouter(prefix="/api/webhooks"), @router.post("/sepay")
# - Đọc header Authorization: Bearer <token>, so sánh với SEPAY_WEBHOOK_AUTH_TOKEN (dùng secrets.compare_digest để chống timing attack — mentor sẽ giải thích khi bạn code).
# - Gọi parse_transfer() -> nếu None thì trả {"status":"ignored"}, nếu có thì ExcelExporter().append() rồi trả {"status":"ok"}.
