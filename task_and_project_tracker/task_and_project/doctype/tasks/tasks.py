# Copyright (c) 2025, Gopinadh Pakala and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class Tasks(Document):
    pass

import frappe
 
def update_status_based_on_subtasks(doc, method):
    try:
        original_status = doc.status
 
        if not doc.subtasks:
            doc.status = 'Pending'
        else:
            all_completed = all(subtask.status == 'Completed' for subtask in doc.subtasks)
 
            if all_completed:
                doc.status = 'Completed'
            else:
                doc.status = 'Pending'
 
        if doc.status != original_status:
            doc.db_set("status", doc.status)
            frappe.msgprint(f"Status updated to: {doc.status}", alert=True)
 
    except frappe.DoesNotExistError:
        frappe.throw(f"The document '{doc.name}' was not found.")
    except Exception as e:
        frappe.log_error(title="Error in update_status_based_on_subtasks", message=frappe.get_traceback())
        frappe.throw(f"An unexpected error occurred: {str(e)}")

 
@frappe.whitelist()
def send_due_date_email(recipient, task_name, due_date):
    subject = f"Task Due Date Reminder: {task_name}"
    message = f"""
        Dear User,<br><br>
        This is a reminder that the task <b>{task_name}</b> due is <b>{due_date} days</b>.<br><br>
        Please take the necessary actions.
    """
    try:
        frappe.sendmail(
            recipients=recipient,
            subject=subject,
            message=message
        )
        return True
    except Exception as e:
        frappe.log_error(f"Error sending email to {recipient}: {str(e)}")
        return False