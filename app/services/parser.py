import re
from app.models.payment import Payment


def parse_transfer(content: str, so_tien: int, thoi_gian: str, transaction_id: str) -> Payment | None:
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
        thoi_gian=thoi_gian,
        ten=ten,
        ma_tham_chieu="THCSC3",
        so_tien=so_tien,
        noi_dung_goc=content,
        transaction_id=transaction_id,
    )