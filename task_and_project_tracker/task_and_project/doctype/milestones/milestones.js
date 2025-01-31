// Copyright (c) 2025, Gopinadh Pakala and contributors
// For license information, please see license.txt

frappe.ui.form.on('Milestones', {
    refresh: function (frm) {
        if (frm.doc.start_date && frm.doc.end_date) {
            calculate_days_between(frm);
        }
    },
    start_date: function (frm) {
        calculate_days_between(frm);
    },
    end_date: function (frm) {
        calculate_days_between(frm);
    }
});
 
function calculate_days_between(frm) {
    const start_date = frm.doc.start_date; 
    const end_date = frm.doc.end_date; 
 
    if (start_date && end_date) {
        const difference_in_days = frappe.datetime.get_diff(end_date, start_date); 
        frm.set_value('deadline_days_remaining', difference_in_days);
    } else {
        frm.set_value('deadline_days_remaining', null); 
    }
}
