from classes.CDay import CDay
import numpy as np

class CWeek:

    days: dict

    def __init__(self):
        self.days = {
            "Monday": CDay(name="Monday"),
            "Tuesday": CDay(name="Tuesday"),
            "Wednesday": CDay(name="Wednesday"),
            "Thursday": CDay(name="Thursday"),
            "Friday": CDay(name="Friday")
        }

    def __str__(self):

        text = ""

        for day_name, day_instance in self.days.items():

            text += str(day_instance) + "\n"

        return text

    def import_meetings(self, meetings_list):

        for meeting in meetings_list:

            if meeting.occurrence == "daily":

                for day_name, day in self.days.items():

                    meeting_name = meeting.name
                    meeting_meet_time = meeting.meet_time
                    meeting_duration = meeting.duration

                    day.timeline[meeting_meet_time] += "," + meeting_name

                    half_hour_steps = float(meeting_duration / 0.5)

                    starting_key = list(day.timeline.keys()).index(meeting_meet_time) + 1

                    for _ in np.arange(0, half_hour_steps):
                        day.timeline[list(day.timeline.keys())[starting_key]] += meeting_name
                        starting_key += 1

            elif meeting.occurrence is None:

                meeting_name = meeting.name
                meeting_day = meeting.day
                meeting_meet_time = meeting.meet_time
                meeting_duration = meeting.duration

                selection_day = self.days[meeting_day]

                selection_day.timeline[meeting_meet_time] += "," + meeting_name

                half_hour_steps = float(meeting_duration / 0.5)

                starting_key = list(selection_day.timeline.keys()).index(meeting_meet_time)

                for _ in np.arange(0, half_hour_steps):

                    selection_day.timeline[list(selection_day.timeline.keys())[starting_key]] += meeting_name
                    starting_key += 1

    def find_overlapping(self, mode=1):
        """Mode 1 returns the overlapping meetings. Mode 2 returns the overbooked people as well as the meetings in
        that overbook them."""
        overlaps = dict()

        if mode == 1:

            overlaps = {
                "Monday": list(),
                "Tuesday": list(),
                "Wednesday": list(),
                "Thursday": list(),
                "Friday": list(),
            }

            # Structure helper: CWeek(days:dict[str,CDay])
            for day_name_week, day_instance in self.days.items():

                # Structure helper: CDay(name: str, timeline:dict[float,str])
                for day_name_self, day_timeline in day_instance:

                    # Structure helper: CDay.timeline(self:dict[float,str])
                    for time_slot, meeting_name in day_timeline.items():

                        overlapping_meetings = meeting_name.split(",")  # Result preview: ["Meeting 1", "Meeting 2"]

                        if len(overlapping_meetings) != 1:  # More than 1 meeting in the time slot
                            overlaps[day_name_self].append(x for x in overlapping_meetings)


        elif mode == 2:
            ...

        return overlaps

    def count_total_number_of_meetings(self):
        ...

    def count_total_hours_in_meetings(self):
        ...

    def count_number_of_meetings_per_owner(self):
        ...
