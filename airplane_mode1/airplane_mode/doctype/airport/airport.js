// Copyright (c) 2024, Shalindra and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airport", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airport', {
    refresh: function(frm) {
        // Fetch and display the list of shop names linked to this airport
        update_shop_names(frm);
    },
    onload: function(frm) {
        // Ensure shop names are updated when the form is loaded
        update_shop_names(frm);
    },
    validate: function(frm) {
        // Ensure the shop names and count are updated before saving
        update_shop_names(frm);
    }
});

function update_shop_names(frm) {
    // Fetch the names of shops linked to this airport
    frappe.call({
        method: 'frappe.client.get_list',
        args: {
            doctype: 'Airport Shop',  // The doctype containing shop details
            filters: { 'airport': frm.doc.name },  // Filter by the current airport ID
            fields: ['shop_name']  // Fetch the 'shop_name' field from Airport Shop
        },
        callback: function(r) {
            if (r.message) {
                // Prepare the list of shop names
                let shop_names = r.message.map(shop => shop.shop_name)  // Join shop names with newline

                // Calculate the total number of shops
                let total_shop = r.message.length;

                // Set the list of shop names in the 'shop_names' field
                frm.set_value('shop_names', shop_names);
                
                // Set the total number of shops in the 'total_shop' field
                frm.set_value('total_shop', total_shop);

                // Refresh the fields to display updated values
                frm.refresh_field('shop_names');
                frm.refresh_field('total_shop');
            }
        }
    });
}
