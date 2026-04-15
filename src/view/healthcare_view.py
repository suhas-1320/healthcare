from src.model.doctor import Doctor
from src.model.patient import Patient


class HealthcareView:
    """
    Handles presentation of healthcare assignments.
    """

    def display_assignments(self, assignments: dict[Patient, Doctor | None]) -> None:
        """
        Displays patient-to-doctor assignments.

        :param assignments: Mapping of patients to doctors
        """
        print("\n--- Patient to Doctor Assignment ---\n")

        for patient, doctor in assignments.items():
            if doctor:
                print(
                    f"Patient Name : {patient.name}\n"
                    f"Disease      : {patient.disease}\n"
                    f"Assigned Doc : Dr. {doctor.name} "
                    f"({doctor.specialization})\n"
                )
            else:
                print(
                    f"Patient Name : {patient.name}\n"
                    f"Disease      : {patient.disease}\n"
                    f"Assigned Doc : No doctor available\n"
                )
