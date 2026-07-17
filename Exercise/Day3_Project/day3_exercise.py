from dataclasses import dataclass
@dataclass
class Invoice:
    invoice_no:int
    name:str
    address:str
    amount:int

class InvoiceController():
    def validate(self,invoice):
        if not invoice.name:
            print("Invalid User")
            return

        if invoice.amount<0:
            print("Amount should be greater than 0")
            return
        print("Valid customer")
        

i1=Invoice(12,"Aniruthra","Kanyakumari",1000)
i2=Invoice(10,"Dharani","Tiruppur",-100)
controller=InvoiceController()
controller.validate(i1)
controller.validate(i2)
