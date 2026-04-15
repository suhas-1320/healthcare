class Doctor:
    """
    Represents a doctor in the healthcare system.
    """

    def __init__(self, doctor_id: int, name: str, specialization: str):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def __repr__(self) -> str:
        return (
            f"Doctor(id={self.doctor_id}, "
            f"name='{self.name}', "
            f"specialization='{self.specialization}')"
        )
