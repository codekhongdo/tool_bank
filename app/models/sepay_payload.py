from pydantic import BaseModel, ConfigDict
from app.models.payment import Payment


class SePayPayload(BaseModel):
    """Model nhận JSON body từ webhook SePay (dạng camelCase, trùng tên trường Payment)."""

    model_config = ConfigDict(populate_by_name=True)

    transactionId: str
    content: str
    amount: int
    transactionDate: str

    def to_payment(self) -> Payment:
        """Chuyển đổi từ SePayPayload sang domain model Payment.

        ten và maThamChieu để rỗng tạm thời, sẽ được điền sau khi
        parser xác nhận có mã THCSC3 trong nội dung chuyển khoản.
        """
        return Payment(
            thoiGian=self.transactionDate,
            ten="",
            maThamChieu="",
            soTien=self.amount,
            noiDungGoc=self.content,
            transactionId=self.transactionId,
        )
