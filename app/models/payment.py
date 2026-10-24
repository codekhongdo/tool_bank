from dataclasses import dataclass


@dataclass
class Payment:
    thoiGian: str
    ten: str
    maThamChieu: str
    soTien: int
    noiDungGoc: str
    transactionId: str

