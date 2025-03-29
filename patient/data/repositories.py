from patient.data.models import Patient
from patient.business.dtos import PatientDTO

def create_patient(dto: PatientDTO):
    patient = Patient.objects.create(
        first_name=dto.first_name,
        last_name=dto.last_name,
        date_of_birth=dto.date_of_birth,
        email=dto.email,
        phone=dto.phone
    )
    return patient
