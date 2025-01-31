# Copyright (c) 2025, Gopinadh Pakala and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data

def get_columns():
    return [
        {"fieldname": "project_name", "label": "Project Name", "fieldtype": "Data", "width": 150},
        {"fieldname": "_of_progress", "label": "% of Progress", "fieldtype": "Percent", "width": 150},
        {"fieldname": "task", "label": "Task Name", "fieldtype": "Link", "width": 100, "options": "Task Details"}
    ]

def get_data(filters):
    conditions = []
    if filters.get("project_name"):
        conditions.append(f" `tabProject Details`.project_name LIKE '%{filters.get('project_name')}%'")
    if filters.get("_of_progress"):
        conditions.append(f" `tabProject Details`._of_progress = {filters.get('_of_progress')}")
    if filters.get("task"):
        conditions.append(f" `tabProject Details`.task LIKE '%{filters.get('task')}%'")

    conditions_query = " AND ".join(conditions) if conditions else "1=1"

    query = f"""
        SELECT
            `tabProject Details`.project_name,
            `tabProject Details`._of_progress,
            `tabProject Details`.task
        FROM
            `tabProject Details`
        WHERE
            {conditions_query}
    """
    data = frappe.db.sql(query, as_dict=True)
    return data