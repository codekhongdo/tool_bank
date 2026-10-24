from app.services.parser import parse_transfer
def test_hop_le():
    p = parse_transfer("NGUYEN VAN A THCSC3", 100000, "2026-10-19 10:00", "tx001")
    assert p is not None
    assert p.ten == "NGUYEN VAN A"
    assert p.maThamChieu == "THCSC3"
    assert p.soTien == 100000
    assert p.noiDungGoc == "NGUYEN VAN A THCSC3"


def test_thieu_ma():
    p = parse_transfer("NGUYEN VAN A", 100000, "2026-10-19 10:00", "tx002")
    assert p is None


def test_hoa_thuong():
    p = parse_transfer("thcsc3 tran thi b", 50000, "2026-10-19 10:00", "tx003")
    assert p is not None
    assert p.ten == "TRAN THI B"