from resources.business.dtos import ResourceDTO
from resources.data.repositories import create_resource as repo_create_resource

def create_resource(data):
    dto = ResourceDTO(**data)
    resource = repo_create_resource(dto)
    return resource
