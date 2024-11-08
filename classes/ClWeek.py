from classes.ClDay import ClDay

class ClWeek:
    """This class manages all work days together as an item."""
    days: dict

    def __init__(self):
        self.days = {
            "Monday": ClDay(name="Monday"),
            "Tuesday": ClDay(name="Tuesday"),
            "Wednesday": ClDay(name="Wednesday"),
            "Thursday": ClDay(name="Thursday"),
            "Friday": ClDay(name="Friday")
        }

    def import_day(self):
        ...

