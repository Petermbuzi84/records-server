import os
import json


class Employee:
    def __init__(self):
        self.employees_path = "database/employees.json"
    
    def save_employee(self, employee):
        employee_list = []
        if os.path.exists(self.employees_path):
            with open(self.employees_path, 'r') as f:
                employee_list = json.load(f)
        employee_list.append(employee)
        self.write_to_employee_list(employee_list)

    def retrieve_employees(self):
        employee_list = []
        if os.path.exists(self.employees_path):
            with open(self.employees_path, 'r') as f:
                employee_list = json.load(f)
        return employee_list

    def update_employee(self, employee_id, n_employee):
        employee_list = retrieve_employees()
        for employee_object in employee_list:
            if employee_object['id_number'] == employee_id:
                employee_list.remove(employee_object)
                employee_list.insert(i, n_employee)
        self.write_to_employee_list(employee_list)

    def delete_employee(self, employee_id):
        employee_list = retrieve_employees()
        for employee_object in employee_list:
            if employee_object['id_number'] == employee_id:
                employee_list.remove(employee_object)
        self.write_to_employee_list(employee_list)
    
    def write_to_employee_list(self, employee_list):
        with open(self.employees_path, 'w') as f:
            json.dump(employee_list, f, indent=True)
