# Copyright (c) 2025, exerp.admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StockTransfer(Document):
	
    def validate(self):
        
        if self.quantity <= 0:
            frappe.throw("Quantity must be a positive value.")

        if self.from_warehouse == self.to_warehouse:
            frappe.throw("From Warehouse and To Warehouse cannot be the same.")