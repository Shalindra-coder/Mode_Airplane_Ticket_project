# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student_me(Document):
	def before_save(self):
		self.full_name = f"{self.first_name}{self.last_name}"

	def validate(self):
		if self.age>25:
			frappe.msgprint("this person age Above 25 this is record succes fully save")
		else:
			frappe.msgprint("please give age above 25")	

