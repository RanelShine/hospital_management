from personnel.business.dtos import PersonnelDTO
from personnel.data.repositories import create_personnel as repo_create_personnel

def create_personnel(data):
    dto = PersonnelDTO(**data)
    personnel_obj = repo_create_personnel(dto)
    return personnel_obj
