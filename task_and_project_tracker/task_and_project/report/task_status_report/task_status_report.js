// Copyright (c) 2025, Gopinadh Pakala and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Task Status Report"] = {
	"filters": [
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nStarted\nIn Progress\nHold\nCompleted",
			"default": " "  
		}
	]
};