# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt
import random
import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    # def before_save(self):
    #     # Generate a random seat number
    #     random_number = random.randint(1, 99)  # Assuming seat numbers range from 1 to 99
    #     random_letter = random.choice('ABCDE')  # Assuming letters A to E for seat allocation
    #     self.seat = f"{random_number}{random_letter}"
    pass

    def before_save(self):
        # Calculate total amount before saving the document
        self.total_amount = self.flight_price + sum(item.amount for item in self.add_ons)

    def before_submit(self):
        # Ensure the ticket status is "Boarded" before submission
        if self.status != "Boarded":
            frappe.throw("Cannot submit the ticket unless it is boarded.")
