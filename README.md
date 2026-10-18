# Tool Bank — SePay THCSC3 Tracker (Mentor Project)

Học viên tự code, Cline làm mentor.

Luồng: Ngân hàng -> SePay Webhook -> FastAPI (verify Bearer) -> Parser Tên + THCSC3 -> Ghi dồn `data/exports/payments.xlsx`.

## Quickstart cho bạn tự làm
1. Copy `.env.example` -> `.env` rồi điền token (xem `docs/setup-sepay.md`).
2. `pip install -r requirements.txt`
3. Tự code theo thứ tự mentor gợi ý:
   - `app/models/payment.py` (class Payment OOP)
   - `app/services/parser.py` (regex THCSC3)
   - `app/services/excel_exporter.py` (openpyxl append)
   - `app/api/webhooks/sepay.py` (FastAPI POST + verify Bearer)
   - `app/main.py` (ghép router)
4. Chạy: `uvicorn app.main:app --reload --port 8000`
5. Test: `pytest`

## Quy tắc
- Không bao giờ đọc `.env`, chỉ đọc `.env.example`.
- Không commit `.xlsx` thật.
- Sau mỗi task xong, update `memory-bank/activeContext.md` + `progress.md`.

Xem thêm: `memory-bank/projectbrief.md`, `docs/setup-sepay.md`, `skills/`.
