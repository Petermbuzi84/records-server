import os
import json
from model.inventory_model import Inventory
from model.employee_model import Employee
from model.sales_model import Sales
from model.service_model import Service


class Database:
    def __init__(self):
        if not os.path.exists('database'):
            os.mkdir('database')

    @property
    def inventory(self):
        return Inventory()
    
    @property
    def sales(self):
        return Sales(Inventory())
    
    @property
    def service(self):
        return Service()
    
    @property
    def employees(self):
        return Employee()
