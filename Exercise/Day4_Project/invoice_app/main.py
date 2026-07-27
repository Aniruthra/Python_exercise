from app import InvoiceService
service=InvoiceService()
total=service.create_invoice()
print(total)