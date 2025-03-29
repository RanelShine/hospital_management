from patient.business.dtos import PatientDTO
from patient.data.repositories import create_patient as repo_create_patient

def create_patient(data):
    dto = PatientDTO(**data)
    patient = repo_create_patient(dto)
    return patient
