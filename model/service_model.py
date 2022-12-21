import os
import json


class Service:
    def __init__(self):
        self.services_path = "database/services.json"

    def save_service(self, service):
        service_list = []
        if os.path.exists(self.services_path):
            with open(self.services_path, 'r') as f:
                service_list = json.load(f)
        service_list.append(service)
        self.write_to_service_list(service_list)

    def retrieve_services(self):
        service_list = []
        if os.path.exists(self.services_path):
            with open(self.services_path, 'r') as f:
                service_list = json.load(f)
        return service_list

    def update_service(self, service_id, n_service):
        service_list = self.retrieve_services()
        for i in range(len(service_list)):
            service_object = service_list[i]
            if service_object['service_id'] == service_id:
                service_list.remove(service_object)
                service_list.insert(i, n_service)
        self.write_to_service_list(service_list)
        
    def delete_service(self, service_id):
        service_list = self.retrieve_services()
        for service_object in service_list:
            if service_object['service_id'] == service_id:
                service_list.remove(service_object)
        self.write_to_service_list(service_list)
    
    def write_to_service_list(self, service_list):
        with open(self.services_path, 'w') as f:
            json.dump(service_list, f, indent=True)
