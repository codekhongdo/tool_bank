from dataclasses import dataclass


@dataclass
class Payment:
    thoi_gian: str
    ten: str
    ma_tham_chieu: str
    so_tien: int
    noi_dung_goc: str
    transaction_id: str

