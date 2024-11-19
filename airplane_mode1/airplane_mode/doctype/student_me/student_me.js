// Copyright (c) 2024, Shalindra and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student_me", {
    refresh(frm) {
        // Ensure that age is a field in the form
        if (frm.doc.age > 25) {
            frappe.throw("This person's age is above 25.");
        } else if (frm.doc.age <= 25 && frm.doc.age !== undefined) {
            frappe.throw("Please fill age above 25. Thank you.");
        }
    }
    
});
