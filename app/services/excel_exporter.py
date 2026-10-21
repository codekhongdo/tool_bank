from pathlib import Path
from openpyxl import Workbook, load_workbook
from app.models.payment import Payment
HEADER = ["thoi_gian", "ten", "ma_tham_chieu", "so_tien", "noi_dung_goc", "transaction_id"]
SHEET_NAME = "payments"


class ExcelExporter:
    def __init__(self, file_path: str = r"d:\tool_bank\data\exports\payments.xlsx"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def _get_workbook_and_sheet(self):
        if self.file_path.exists():
            wb = load_workbook(self.file_path)
            if SHEET_NAME in wb.sheetnames:
                ws = wb[SHEET_NAME]
            else:
                ws = wb.create_sheet(SHEET_NAME)
                ws.append(HEADER)
        else:
            wb = Workbook()
            ws = wb.active 
            ws.title = SHEET_NAME
            ws.append(HEADER)
        return wb, ws

    def _is_duplicate(self, ws, transaction_id: str) -> bool:
        for row in ws.iter_rows(min_row=2, values_only=True):
            if row[5] == transaction_id:
                return True
        return False

    def append(self, payment: Payment) -> bool:
        wb, ws = self._get_workbook_and_sheet()
        if self._is_duplicate(ws, payment.transaction_id):
            return False
        ws.append(
            [
                payment.thoi_gian,
                payment.ten,
                payment.ma_tham_chieu,
                payment.so_tien,
                payment.noi_dung_goc,
                payment.transaction_id,
            ]
        )
        wb.save(self.file_path)
        return True

