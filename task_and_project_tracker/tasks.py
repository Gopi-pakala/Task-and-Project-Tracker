import frappe
from frappe.email.queue import flush
 
def check_and_send_project_notifications():
 
    projects = frappe.get_all(
        "Project Details",
        fields=["name", "project_name", "description", "project_manager"]
    )
 
    if not projects:
        frappe.logger().info("No projects found.")
        return
    for project in projects:
        if not project.project_manager:
            frappe.logger().warning(f"No project manager found for project {project.project_name}")
            continue
        subject = f"Project Notification for {project.project_name}"
        message = f"""
<p>Dear {project.project_manager},</p>
<p>The following project details are available for your attention:</p>
<p><b>Project Name:</b> {project.project_name}</p>
<p><b>Description:</b> {project.description}</p>
<p>Please review and take necessary action.</p>
<br>
<p>Regards,<br>Project Management Team</p>
        """
 
        try:
            frappe.sendmail(
                recipients=project.project_manager,
                subject=subject,
                message=message
            )
            frappe.logger().info(f"Email queued for {project.project_manager} regarding {project.project_name}")
 
        except Exception as e:
            frappe.log_error(f"Error sending email to {project.project_manager}: {str(e)}")
            frappe.logger().error(f"Failed to queue email for {project.project_name}: {str(e)}")
 

    frappe.enqueue(method=flush, queue="short")
    frappe.logger().info("Email queue flushed and emails sent.")
 
    frappe.db.commit()