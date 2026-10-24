import re
from app.models.payment import Payment


def parse_transfer(content: str, soTien: int, thoiGian: str, transactionId: str) -> Payment | None:
    upper_content = content.upper()
    if "THCSC3" not in upper_content:
        return None
    m = re.search(r"(.*)THCSC3(.*)", upper_content)
    if not m:
        return None
    before = " ".join(m.group(1).split())
    after = " ".join(m.group(2).split())
    ten = before if before else after
    if not ten:
        return None
    return Payment(
        thoiGian=thoiGian,
        ten=ten,
        maThamChieu="THCSC3",
        soTien=soTien,
        noiDungGoc=content,
        transactionId=transactionId,
    )