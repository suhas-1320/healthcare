class Patient:
    """
    Represents a patient with a diagnosed disease.
    """

    def __init__(self, patient_id: int, name: str, disease: str):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease

    def __repr__(self) -> str:
        return (
            f"Patient(id={self.patient_id}, "
            f"name='{self.name}', "
            f"disease='{self.disease}')"
        )