// Copyright (c) 2024, Shalindra and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gate Number", {
	refresh(frm) {
        frappe.call({
            method: "your_app.gate_number.update_gate_number",
            args: {
                gate_number_name: "G1",  // Existing gate number name
                new_gate_number: "G2",    // New gate number
                flight: "Flight 101",      // Associated flight
                boarding_time: "2024-10-30 14:30:00" // New boarding time
            },
            callback: function(r) {
                if (!r.exc) {
                    frappe.msgprint(__("Gate number updated successfully!"));
                }
            }
        });
        

	},
});
