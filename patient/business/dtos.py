class PatientDTO:
    def __init__(self, first_name, last_name, date_of_birth, email, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
