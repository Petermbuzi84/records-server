import json
from database import Database
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
data = Database()


#######################
# inventory 
#######################
@app.route('/add_inventory', methods=['POST'])
def add_inventory():
    inventory_data = request.get_json()
    data.inventory.save_inventory(inventory_data)
    return {"data": "ok"}


@app.route('/update_inventory/<string:item_id>', methods=['POST'])
def update_inventory(item_id):
    data.inventory.update_inventory(item_id, request.get_json())
    return {"data": "ok"}


@app.route('/', methods=['GET'])
def inventory():
    return {"inventory": data.inventory.retrieve_inventory()}


@app.route('/inventory', methods=['GET'])
def inventory():
    return {"inventory": data.inventory.retrieve_inventory()}


@app.route('/search_inventory/<string:query>', methods=['GET'])
def search_inventory(query):
    inventory_list = data.inventory.retrieve_inventory()
    query_list = []
    for item in inventory_list:
        if item['item'].lower().__contains__(query.lower()):
            query_list.append(item)
    return {"search": query_list}


@app.route('/delete_inventory/<string:item_id>', methods=['GET'])
def delete_inventory(item_id):
    data.inventory.delete_inventory(item_id)
    return {'data': 'ok'}


#######################
# employee 
#######################
@app.route('/add_employee', methods=['POST'])
def add_employee():
    employee_data = request.get_json()
    data.employees.save_employee(employee_data)
    return {"data": "ok"}


@app.route('/search_employees/<string:query>', methods=['GET'])
def search_employees(query):
    employee_list = data.employees.retrieve_employees()
    query_list = []
    for employee in employee_list:
        if employee['first_name'].lower().__contains__(query.lower()):
            query_list.append(employee)
        elif employee['last_name'].lower().__contains__(query.lower()):
            query_list.append(employee)
    return {"search": query_list}


@app.route('/update_employee/<int:employee_id>', methods=['POST'])
def update_employee(employee_id):
    data.employees.update_employee(employee_id, request.get_json())
    return {"data": "ok"}


@app.route('/delete_employee/<int:employee_id>', methods=['GET'])
def delete_employee(employee_id):
    data.employees.delete_employee(employee_id)
    return {"data": "ok"}


@app.route('/employees', methods=['GET'])
def employees():
    return {"employees": data.employees.retrieve_employees()}


#######################
# sale 
#######################
@app.route('/add_sale', methods=['POST'])
def add_sale():
    sale_data = request.get_json()
    data.sales.save_sale(sale_data)
    return {"data": "ok"}


@app.route('/search_sales/<string:query>', methods=['GET'])
def search_sales(query):
    sale_list = data.sales.retrieve_sales()
    query_list = []
    for sale in sale_list:
        if sale['item'].lower().__contains__(query.lower()):
            query_list.append(sale)
    return {"search": query_list}


@app.route('/update_sale/<string:sale_id>', methods=['POST'])
def update_sale(sale_id):
    sale_data = request.get_json()
    data.sales.update_sale(sale_id, sale_data)
    return {"data": "ok"}


@app.route('/delete_sale/<string:sale_id>', methods=['GET'])
def delete_sale(sale_id):
    data.sales.delete_sale(sale_id)
    return {'data': 'ok'}


@app.route('/sales', methods=['GET'])
def sales():
    return {"sales": data.sales.retrieve_sales()}


#######################
# service 
#######################
@app.route('/add_service', methods=['POST'])
def add_service():
    service_data = request.get_json()
    data.service.save_service(service_data)
    return {"data": "ok"}


@app.route('/search_services/<string:query>', methods=['GET'])
def search_services(query):
    service_list = data.service.retrieve_services()
    query_list = []
    for service in service_list:
        if service['service'].lower().__contains__(query.lower()):
            query_list.append(service)
    return {"search": query_list}


@app.route('/services', methods=['GET'])
def services():
    return {"services": data.service.retrieve_services()}


@app.route('/update_service/<string:service_id>', methods=['POST'])
def update_service(service_id):
    service_data = request.get_json()
    data.service.update_service(service_id, service_data)
    return {"data": "ok"}


@app.route('/delete_service/<string:service_id>', methods=['GET'])
def delete_service(service_id):
    data.service.delete_service(service_id)
    return {'data': 'ok'}


if __name__ == '__main__':
    app.run()