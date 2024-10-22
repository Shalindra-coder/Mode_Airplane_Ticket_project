// Copyright (c) 2024, Shalindra and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button(__('Assign Seat'), function() {
            const d = new frappe.ui.Dialog({
                title: 'Assign Seat',
                fields: [
                    {
                        fieldtype: 'Data',
                        fieldname: 'seat_number',
                        label: 'Seat Number',
                        reqd: 1
                    }
                ],
                primary_action: function() {
                    const values = d.get_values();
                    frm.set_value('seat', values.seat_number);
                    d.hide();
                }
            });
            d.show();
        });
    }
});
