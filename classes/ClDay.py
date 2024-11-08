import numpy as np


class ClDay:
    """Container for one day's meetings per time slot and corresponding meeting owners."""

    name: str
    timeline: dict

    def __init__(self, name="") -> None:
        self.name = name
        self.timeline = {float(x): list() for x in np.arange(9.0, 19.0, 0.5)}

    def import_meeting(self, name, meet_time, duration, owner) -> None:

        if type(name) != str:
            raise ValueError

        if type(meet_time) != float:
            raise ValueError

        if type(duration) != float:
            raise ValueError

        if type(owner) != str:
            raise ValueError

        i = list(self.timeline.keys()).index(meet_time)

        for _ in np.arange(duration / 0.5):
            self.timeline[list(self.timeline.keys())[i]].append((name, owner))
            i += 1

    def find_conflicts(self) -> dict:

        result = dict()
        # result: { }

        concurrent_meetings = list()
        overbooked_pms = list()

        for time_slot, meeting_list in self.timeline.items():
            """
            timeslot: float
            meeting_list: [ tuple('meet_name', meet_owner'), ... ]
            """

            owners_in_current_timeslot = (
                list()
            )  # gets reset on every time slot iteration
            concurrent_meetings_in_current_timeslot = (
                list()
            )  # gets reset on every time slot iteration

            # the 3 variables below created here iteratively,
            # as we cycle through all the indeces of the "timeline"
            # dictionary of the current day
            result[time_slot] = dict()
            result[time_slot]["Meetings"] = list()
            result[time_slot]["PMs"] = list()
            # result: { time_slot: { "PMs": [], "Meetings": [] }, }

            if len(meeting_list) > 1:

                for meet_tuple in meeting_list:
                    """
                    meet_tuple: (name, owner)
                    """

                    meeting_name = meet_tuple[0]
                    meeting_owner = meet_tuple[1]

                    concurrent_meetings_in_current_timeslot.append(meeting_name)
                    owners_in_current_timeslot.append(meeting_owner)

            if (
                len(concurrent_meetings_in_current_timeslot) > 1
            ):  # no reason to run iteration if list is empty
                for each_meeting in concurrent_meetings_in_current_timeslot:
                    result[time_slot]["Meetings"].append(each_meeting)

            overbooked_pms_in_this_timeslot = list(
                set(
                    [
                        owner
                        for owner in owners_in_current_timeslot
                        if owners_in_current_timeslot.count(owner) > 1
                    ]
                )
            )

            if (
                len(overbooked_pms_in_this_timeslot) > 0
            ):  # no reason to run iteration if list is empty
                for pm in overbooked_pms_in_this_timeslot:
                    if result.get(time_slot) is not None:
                        result[time_slot]["PMs"].append(pm)

        return result
