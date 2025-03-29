from personnel.data.models import Personnel
from personnel.business.dtos import PersonnelDTO

def create_personnel(dto: PersonnelDTO):
    personnel_obj = Personnel.objects.create(
        first_name=dto.first_name,
        last_name=dto.last_name,
        role=dto.role,
        email=dto.email
    )
    return personnel_obj
