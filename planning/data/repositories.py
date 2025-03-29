from planning.data.models import Appointment
from planning.business.dtos import AppointmentDTO
from patient.data.models import Patient

def create_appointment(dto: AppointmentDTO):
    patient = Patient.objects.get(pk=dto.patient_id)
    appointment = Appointment.objects.create(
        patient=patient,
        date=dto.date,
        description=dto.description
    )
    return appointment
