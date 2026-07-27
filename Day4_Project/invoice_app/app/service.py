from .models import Invoice
from .repository import InvoiceRepository

class InvoiceService:
    def __init__(self):
        self.repo=InvoiceRepository()

    def create_invoice(self):
        invoice=Invoice(101,"Ani",1500)
        total=invoice.amount*0.18
        self.repo.save(invoice)
        return total