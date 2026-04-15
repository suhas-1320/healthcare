from src.model.doctor import Doctor
from src.model.patient import Patient
from src.service.assignment_service import AssignmentService
from src.view.healthcare_view import HealthcareView


def main() -> None:
    """
    Entry point for the Healthcare application.
    Creates doctors and patients, assigns doctors to patients,
    and displays the results.
    """

    # Create doctors
    doctors = [
        Doctor(1, "Alice", "Cardiology"),
        Doctor(2, "Bob", "Dermatology"),
        Doctor(3, "Charlie", "Neurology"),
    ]

    # Create patients
    patients = [
        Patient(1, "John", "Cardiology"),
        Patient(2, "Emma", "Dermatology"),
        Patient(3, "Liam", "Orthopedics"),
    ]

    # Assign doctors to patients
    assignment_service = AssignmentService()
    assignments = assignment_service.assign_doctors(patients, doctors)

    # Display the assignments
    view = HealthcareView()
    view.display_assignments(assignments)


if __name__ == "__main__":
    main()
