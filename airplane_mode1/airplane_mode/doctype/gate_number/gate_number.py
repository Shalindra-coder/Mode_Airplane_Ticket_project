# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class GateNumber(Document):
# 	pass
import frappe
from frappe import _

# Doctype definition
class GateNumber(frappe.model.document.Document):
    pass

@frappe.whitelist()
def update_gate_number(gate_number_name, new_gate_number, flight, boarding_time):
    gate_number = frappe.get_doc("Gate Number", gate_number_name)
    
    if gate_number:
        gate_number.gate_number = new_gate_number
        gate_number.flight = flight
        gate_number.boarding_time = boarding_time
        gate_number.save()
        frappe.msgprint(_("Gate number updated successfully!"))
    else:
        frappe.throw(_("Gate number record not found!"))

