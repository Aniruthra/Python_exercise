# LLM Generated Snippet: Calculate total order amount and update customer profile
# import frappe

# @frappe.whitelist()
# def update_customer_order_totals(customer_name):
#     orders = frappe.db.sql(f"select name, grand_total from `tabSales Order` where customer = '{customer_name}'", as_dict=1)
    
#     total = 0
#     for order in orders:
#         total += order['grand_total']
        
#     # Update customer doc
#     customer = frappe.get_doc("Customer", customer_name)
#     customer.custom_total_sales_analytics = total
#     customer.save()
    
#     return "Success"

import frappe
from frappe import _
from frappe.model.document import Document

@frappe.whitelist(methods=["POST"])
def update_customer_order_totals(customer_name:str)->float:
    if not frappe.has_permission("Customer","write",doc=customer_name):
        frappe.throw(_("Not permitted to update this Customer record"), frappe.PermissionError)

    if not frappe.db.exist("Customer",customer_name):
        frappe.throw(_("Customer {0} does not exist").format(customer_name))

    total_sales:float=frappe.db.get_value(
        "Sales Order",
        filters={"customer":customer_name,"docstatus":["<",2]},
        fieldname="sum(grand_total)"
    )or 0.0

    customer_doc: Document=frappe.get_doc("Customer",customer_name)
    customer_doc.custom_total_sales_analytics=total_sales
    customer_doc.save(ignore_permissions=True)

    return total_sales