# Tool Bank — SePay THCSC3 Tracker

Ứng dụng FastAPI nhận webhook biến động số dư từ SePay, lọc nội dung chuyển khoản có mã `THCSC3`, sau đó ghi dữ liệu hợp lệ vào một file Excel duy nhất.

## Luồng hoạt động

```text
Ngân hàng → SePay → FastAPI webhook → xác thực token → parser THCSC3 → payments.xlsx
```

Endpoint nhận webhook:

```text
POST /api/webhooks/sepay
```

Endpoint kiểm tra server:

```text
GET /health
```

## Công nghệ

- Python 3.10+
- FastAPI và Uvicorn
- Pydantic Settings
- openpyxl
- pytest
- Ngrok để expose server local qua HTTPS

## Cài đặt

Từ thư mục dự án `d:\tool_bank`:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Tạo file cấu hình local từ file mẫu:

```powershell
Copy-Item .env.example .env
```

Sau đó điền các giá trị thật vào `.env`:

```env
SEPAY_API_TOKEN=your_sepay_api_token
SEPAY_WEBHOOK_AUTH_TOKEN=your_webhook_secret
BANK_ACCOUNT_NUMBER=your_bank_account
EXPECTED_CODE=THCSC3
EXCEL_OUTPUT_DIR=data/exports
EXCEL_FILE_NAME=payments.xlsx
APP_HOST=127.0.0.1
APP_PORT=8000
```

Không commit `.env` hoặc token lên Git.

## Chạy kiểm thử

```powershell
pytest -v
```

Test hiện có kiểm tra:

- Parser nhận diện đúng hoặc loại nội dung thiếu `THCSC3`.
- Token sai trả `401` trước khi xử lý body.
- Nhiều webhook đồng thời không làm hỏng file Excel.
- Cùng một `transaction_id` chỉ được ghi một lần.

## Chạy server local

```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Kiểm tra endpoint health trong terminal khác:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

Kết quả mong muốn:

```json
{"status":"ok"}
```

## Payload webhook

Code hiện tại đọc các trường SePay sau:

```json
{
  "content": "NGUYEN VAN A THCSC3",
  "transferAmount": 10000,
  "transactionDate": "2026-10-25 10:00:00",
  "id": "transaction-001"
}
```

Header xác thực:

```text
Authorization: Bearer <SEPAY_WEBHOOK_AUTH_TOKEN>
```

Phản hồi thành công:

```json
{"success":true,"status":"ok"}
```

Các trạng thái khác:

- `ignored`: nội dung không có mã `THCSC3`.
- `duplicate`: `id` đã tồn tại trong Excel.

## Expose bằng Ngrok

Giữ Uvicorn đang chạy, mở terminal khác:

```powershell
ngrok http 8000
```

Dùng URL HTTPS Ngrok trong cấu hình SePay:

```text
https://your-ngrok-domain.ngrok-free.app/api/webhooks/sepay
```

SePay cần gửi header `Authorization` với đúng token trong `.env`.

## File Excel

Dữ liệu được ghi vào:

```text
data/exports/payments.xlsx
```

Sheet:

```text
payments
```

Các cột:

```text
thoiGian | ten | maThamChieu | soTien | noiDungGoc | transactionId
```

Không mở `payments.xlsx` bằng Excel trong lúc server đang nhận webhook. Excel có thể khóa file và khiến `openpyxl` gặp lỗi `PermissionError` khi lưu.

## Cấu trúc chính

```text
app/
├── api/webhooks/sepay.py       # HTTP endpoint và xác thực
├── core/config.py              # Đọc cấu hình từ .env
├── models/payment.py           # Payment dataclass
├── services/parser.py          # Lọc và tách nội dung THCSC3
├── services/excel_exporter.py  # Ghi Excel và chống trùng
└── main.py                     # Khởi tạo FastAPI

tests/
├── test_parser.py
└── test_webhook.py
```

## Lưu ý bảo mật và vận hành

- Không hardcode token trong source code.
- Không commit `.env` hoặc file Excel chứa dữ liệu thật.
- Dùng giao dịch nhỏ khi kiểm thử thật.
- URL Ngrok miễn phí có thể thay đổi sau mỗi lần khởi động.
- Máy chạy Uvicorn và Ngrok phải luôn bật để nhận webhook.
