from dataclasses import dataclass

@dataclass
class Invoice:
    invoice_no: int
    customer: str
    amount: float


