class InvoiceRepository:
    def save(self, invoice):
        print(f"Saving invoice {invoice.invoice_no}")