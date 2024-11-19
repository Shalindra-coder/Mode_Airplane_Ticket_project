# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class api_test(Document):
    def before_save(self):
        self.update_total_days()

    def update_total_days(self):
        new_data_records = frappe.get_all(
            'new_data',
            fields=['email', 'address', 'day']  
        )
        total_days = sum(record['day'] for record in new_data_records)
        self.total_days = total_days
        


