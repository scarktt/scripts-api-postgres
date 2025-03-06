class Report:
    def __init__(self, location: str, unemployed_per_location: int):
        self.location = location
        self.unemployed_per_location = unemployed_per_location

    def to_dict(self):
        return {
            "location": self.location,
            "unemployed_per_location": self.unemployed_per_location,
        }
