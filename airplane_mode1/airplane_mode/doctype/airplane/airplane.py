# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):
   def validate_ticket_capacity(ticket):
    flight = frappe.get_doc("Airplane Flight", ticket.flight)
    current_tickets = frappe.db.count("Airplane Ticket", {"flight": ticket.flight})

    if current_tickets >= flight.capacity:
        frappe.throw("Cannot create ticket. The flight is fully booked.")
