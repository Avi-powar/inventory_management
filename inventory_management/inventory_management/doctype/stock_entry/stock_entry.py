# Copyright (c) 2025, exerp.admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import throw

class Stockentry(Document):
    def validate(self):
        if self.quantity <=0:
            frappe.throw("quantity must be positive value.")

    # def before_save(self):
    #     self.fill_into()
        
            
        
    @frappe.whitelist()   
    def fill_into(self):
        if self.entry_type== "Stock In":
	        quantity_change = self.quantity
        elif self.entry_type=="Stock Out":
            quantity_change = -self.quantity
        else:
            quantity_change=0
            
        
        sle = frappe.new_doc("Stock Book")
        
        sle.item=self.item
        sle.warehouse =self.warehouse
        sle.transaction_type =self.entry_type
        sle.quantity_change = quantity_change
        sle.stock_entry = self.name
        
        sle.insert()
            
        
        
