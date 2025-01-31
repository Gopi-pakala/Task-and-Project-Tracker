// Copyright (c) 2025, Gopinadh Pakala and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project Details', {
    project_type(frm) {
        const projectType = frm.doc.project_type;

        if (projectType === 'External') {
            frm.set_value('priority', 'Critical');
        } else if (projectType === 'Internal') {
            frm.set_value('priority', 'High');
        } else if (projectType === 'Other') {
            frm.set_value('priority', 'Low'); 
        }
    }
});
