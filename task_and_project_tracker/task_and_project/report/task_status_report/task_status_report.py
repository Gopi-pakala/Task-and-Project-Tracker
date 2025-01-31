# Copyright (c) 2025, Gopinadh Pakala and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data

def get_columns():
    return [
        {"fieldname": "task_name", "label": "Task Name", "fieldtype": "Data", "width": 150},
        {"fieldname": "assigned_to", "label": "Assigned To", "fieldtype": "Data", "width": 150},
        {"fieldname": "status", "label": "Status", "fieldtype": "Select", "width": 100},
        {"fieldname": "start_date", "label": "Start Date", "fieldtype": "Date", "width": 120},
        {"fieldname": "end_date", "label": "End Date", "fieldtype": "Date", "width": 120},
        {"fieldname": "completion_date", "label": "Completion Date", "fieldtype": "Date", "width": 120},
    ]

def get_data(filters):
    conditions = []
    if filters.get("task_name"):
        conditions.append(f"tasks.task_name LIKE '%{filters.get('task_name')}%'")
    if filters.get("assigned_to"):
        conditions.append(f"tasks.assigned_to = '{filters.get('assigned_to')}'")
    if filters.get("status"):
        conditions.append(f"tasks.status = '{filters.get('status')}'")
    if filters.get("start_date"):
        conditions.append(f"tasks.start_date >= '{filters.get('start_date')}'")
    if filters.get("end_date"):
        conditions.append(f"tasks.end_date <= '{filters.get('end_date')}'")
    if filters.get("completion_date"):
        conditions.append(f"tasks.completion_date = '{filters.get('completion_date')}'")

    conditions_query = " AND ".join(conditions) if conditions else "1=1"

    query = f"""
        SELECT
            tasks.task_name,
            tasks.assigned_to,
            tasks.status,
            tasks.start_date,
            tasks.end_date,
            tasks.completion_date
        FROM
            `tabTasks` tasks
        WHERE
            {conditions_query}
    """
    data = frappe.db.sql(query, as_dict=True)
    return data