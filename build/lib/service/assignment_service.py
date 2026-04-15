from src.model.doctor import Doctor
from src.model.patient import Patient


class AssignmentService:
    """
    Handles business logic for assigning patients to doctors
    based on disease and specialization.
    """

    def assign_doctors(
        self,
        patients: list[Patient],
        doctors: list[Doctor],
    ) -> dict[Patient, Doctor | None]:
        """
        Assigns each patient to a doctor whose specialization
        matches the patient's disease.

        :param patients: List of patients
        :param doctors: List of doctors
        :return: Dictionary mapping Patient to Doctor (or None if no match)
        """
        assignments: dict[Patient, Doctor | None] = {}

        for patient in patients:
            matched_doctor = None

            for doctor in doctors:
                if doctor.specialization.lower() == patient.disease.lower():
                    matched_doctor = doctor
                    break

            assignments[patient] = matched_doctor

        return assignments