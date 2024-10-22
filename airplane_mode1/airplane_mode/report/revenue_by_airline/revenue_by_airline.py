# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

def execute(filters=None):

    # Define columns for the report
    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airplane", "width": 150},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
    ]

    # Fetch revenue data for each airline using SQL query
    ticket_data = frappe.db.sql("""
        SELECT a.airline, 
               COALESCE(SUM(b.total_amount), 0) AS total_amount
        FROM tabAirplane a
        LEFT JOIN `tabAirplane Ticket` b ON b.flight LIKE CONCAT('%', a.name, '%')
        GROUP BY a.airline
    """, as_dict=True)

    # Convert ticket data into a dictionary for easier lookup
    airline_revenue = {ticket['airline']: flt(ticket['total_amount']) for ticket in ticket_data}

    # Calculate total revenue
    total_revenue = sum(airline_revenue.values())

    # Create the data list
    data = []
    for airline in airline_revenue.keys():
        data.append({
            "airline": airline,
            "revenue": airline_revenue[airline]
        })

    # Create Donut Chart data
    chart = {
        "data": {
            "labels": [d['airline'] for d in data],
            "datasets": [{"values": [airline_revenue[d['airline']] for d in data]}],
        },
        "type": "donut",
    }

    # Return the columns, data, chart, and total revenue as a separate summary
    return columns, data, None, chart, [{"label": "Total Revenue", "value": total_revenue, "datatype": "Currency", "indicator": "green"}]
