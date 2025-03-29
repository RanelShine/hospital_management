from planning.business.dtos import AppointmentDTO
from planning.data.repositories import create_appointment as repo_create_appointment

def create_appointment(data):
    dto = AppointmentDTO(**data)
    appointment = repo_create_appointment(dto)
    return appointment
