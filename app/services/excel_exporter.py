# TODO cho bạn tự code: class ExcelExporter (openpyxl, file dồn payments.xlsx)
# Gợi ý:
# - __init__(self, file_path): lưu đường dẫn dồn duy nhất data/exports/payments.xlsx
# - append(payment): mở file nếu có, chưa có thì tạo + ghi header [thoi_gian, ten, ma_tham_chieu, so_tien, noi_dung_goc, transaction_id], check trùng transaction_id rồi mới append.
# - Tại sao 1 file dồn: bạn đã chọn, dễ đối soát, nhưng phải chống trùng.
