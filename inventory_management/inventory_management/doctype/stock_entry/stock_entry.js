// Copyright (c) 2025, exerp.admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Stock entry", {
	after_save(frm) {
        frm.call({
            method: 'fill_into',
            doc : frm.doc
        })
	},
});
