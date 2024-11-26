import frappe
from datetime import datetime, timedelta

def send_monthly_rent_reminder():
    # Get today's date and calculate tomorrow's date for comparison
    today = datetime.today()
    day_before_due = today + timedelta(days=1)  # One day before the due date
    
    # Fetch all the tenants from the "Rent Payment" doctype
    rent_data = frappe.get_all("Rent Payment", fields=["email", "payment_amount", "tenant_name", "shop_number", "disable", "due_date"])

    # Loop through each tenant record and send email
    for tenant in rent_data:
        # Skip tenant if email is disabled
        if tenant.get("disable"):
            continue  # Skip this tenant if the "disable" field is True

        # Fetch the tenant's details
        email = tenant.get("email")
        payment_amount = tenant.get("payment_amount")
        tenant_name = tenant.get("tenant_name")
        shop_number = tenant.get("shop_number")
        due_date = tenant.get("due_date")

        # Convert the due_date to a datetime object if it's a string
        if isinstance(due_date, str):
            due_date = datetime.strptime(due_date, '%Y-%m-%d')  # Adjust the format if needed

        # Check if today's date is one day before the due date
        if due_date - timedelta(days=1) == today.date():  # Ensure to compare dates without the time component
            # Compose the content for the email
            content = f"""
            This is a reminder to pay your rent for this month.

            Amount: {payment_amount}
            Tenant Name: {tenant_name}
            Shop Number: {shop_number}

            Please make sure to pay your rent on time.
            """

            # Sending the email to the tenant
            frappe.sendmail(
                recipients=email,  # Tenant's email
                cc='',  # Add CC if needed
                subject='Reminder: Pay your due rent',
                content=content,
                reference_doctype='Rent Payment',  # Reference to the Rent Payment doctype
                reference_name=None,  # You can add the document name if needed
                now=True  # Send the email immediately
            )

    # Confirmation message after emails are sent
    frappe.msgprint("Monthly rent reminders have been sent successfully.")


