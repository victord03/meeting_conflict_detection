"""Main file for ClWeek class"""

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

    def import_meeting(self, meeting):
            meeting_name = meeting[0]
            meeting_time = meeting[1]
            meeting_duration = meeting[2]
            meeting_owner = meeting[3]
            meeting_day = meeting[4]

            if not self.days.get(meeting_day):
                raise ValueError
            else:
                self.days[meeting_day].import_meeting(meeting_name, meeting_time, meeting_duration, meeting_owner)
