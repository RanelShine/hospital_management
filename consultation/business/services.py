from consultation.business.dtos import ConsultationDTO
from consultation.data.repositories import create_consultation as repo_create_consultation

def create_consultation(data):
    dto = ConsultationDTO(**data)
    consultation = repo_create_consultation(dto)
    return consultation
