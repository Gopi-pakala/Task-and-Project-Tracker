// Copyright (c) 2025, Gopinadh Pakala and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Project Progress Report"] = {
    "filters": [
        {
            "fieldname": "task",
            "label": __("Task Name"),
            "fieldtype": "Link",
            "options": "Task Details"
        }
    ]
};