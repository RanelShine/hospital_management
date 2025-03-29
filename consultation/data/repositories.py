from consultation.data.models import Consultation
from consultation.business.dtos import ConsultationDTO
from patient.data.models import Patient

def create_consultation(dto: ConsultationDTO):
    patient = Patient.objects.get(pk=dto.patient_id)
    consultation = Consultation.objects.create(
        patient=patient,
        date=dto.date,
        notes=dto.notes
    )
    return consultation
