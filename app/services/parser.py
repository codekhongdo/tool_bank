# TODO cho bạn tự code: def parse_transfer(content: str, ...) -> Payment | None
# Gợi ý mentor (không code full):
# 1. upper() content để tìm THCSC3 không phân biệt hoa thường — tại sao: user gõ thcsc3 vẫn phải nhận.
# 2. dùng regex r"(.*)THCSC3" để tách tên — tại sao regex: linh hoạt khoảng trắng, vị trí mã.
# 3. strip() tên, nếu rỗng hoặc thiếu mã -> return None (loại, không ghi excel).
# Bạn tự code 10-15 dòng, test với "NGUYEN VAN A THCSC3".
