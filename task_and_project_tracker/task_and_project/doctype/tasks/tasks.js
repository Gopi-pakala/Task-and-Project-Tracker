// Copyright (c) 2025, Gopinadh Pakala and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tasks', {
	refresh: function (frm) {
		frm.add_custom_button('Send Due Date Notifications', function () {
			function check_and_send_email() {
				if (frm.doc.due_date && frm.doc.due_date > 0 && frm.doc.assigned_to) {
					frappe.call({
						method: "task_and_project_tracker.task_and_project.doctype.tasks.tasks.send_due_date_email",
						args: {
							recipient: frm.doc.assigned_to,
							task_name: frm.doc.task_name,
							due_date: frm.doc.due_date,
						},
						callback: function (response) {
							if (response.message) {
								frappe.msgprint(`Email sent to ${frm.doc.assigned_to}`);
							} else {
								frappe.msgprint(`Failed to send email to ${frm.doc.assigned_to}`);
							}
						},
						error: function (error) {
							frappe.msgprint(`Error sending email to ${frm.doc.assigned_to}`);
						},
					});
				} else {
					frappe.msgprint("Please ensure both 'Due Date' and 'Assigned To' fields are filled.");
				}
			}
			check_and_send_email();
		});
	},
});

frappe.ui.form.on('Tasks', {
    refresh: function(frm) {
        update_alert_field(frm);
    },
    end_date: function(frm) {
        update_alert_field(frm);
    }
});

function update_alert_field(frm) {
    if (frm.doc.end_date) {
        let today = frappe.datetime.get_today();
        let end_date = frm.doc.end_date;
        let days_difference = frappe.datetime.get_day_diff(end_date, today);

        frm.set_value('alert', days_difference);
    }
}

frappe.ui.form.on('Tasks', {
    end_date: function (frm) {
        update_due_date(frm);
    }
});

function update_due_date(frm) {
    const today = frappe.datetime.get_today();
    const end_date = frm.doc.end_date;

    if (!end_date) {
        frm.set_value('due_date', null);
        return;
    }

    const difference_in_days = frappe.datetime.get_diff(today, end_date);

    if (difference_in_days > 0) {
        frm.set_value('due_date', difference_in_days);
    } else {
        frm.set_value('due_date', null);
    }
}



frappe.ui.form.on('Tasks', {
    end_date: function (frm) {
        if (frm.doc.start_date && frm.doc.end_date) {
            let date1 = new Date(frm.doc.start_date);
            let date2 = new Date(frm.doc.end_date);
            let diffInMilliseconds = date2 - date1;
 
            let diffInHours = diffInMilliseconds / (1000 * 60 * 60);
 
            frappe.msgprint({
                message: __('The number of hours between the dates is: {0}', [diffInHours]),
            });
 
            frm.set_value('estimated_hours', diffInHours);
        } else {
            frappe.msgprint({
                message: __('Please select both Date 1 and Date 2 to calculate the hours.'),
            });
        }
    }
});
