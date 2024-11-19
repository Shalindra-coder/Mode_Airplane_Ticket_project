import frappe

def send_monthly_rent_reminder():
    # Fetch all the tenants from the "Rent Payment" doctype
    rent_data = frappe.get_all("Rent Payment", fields=["email", "payment_amount", "tenant_name", "shop_number", "disable"])
    
    # Loop through each tenant record and send email
    for tenant in rent_data:
        # Check if tenant's email is disabled, if so, skip sending email
        if tenant.get("disable"):
            continue  # Skip this tenant if the "disable" field is True
        
        email = tenant.get("email")
        payment_amount = tenant.get("payment_amount")
        tenant_name = tenant.get("tenant_name")
        shop_number = tenant.get("shop_number")
        
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
            # sender='shalindraaporiya0088@gmail.com'
            cc='',  # Add CC if needed
            subject='Reminder: Pay your due rent',
            content=content,
            reference_doctype='Rent Payment',  # Reference to the Rent Payment doctype
            reference_name=None,  # You can add the document name if needed
            now=True  # Send the email immediately
        )

    # Confirmation message after emails are sent
    frappe.msgprint("Monthly rent reminders have been sent successfully.")
