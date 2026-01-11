"""Main module"""

from classes.ClWeek import ClWeek
from data.meeting_names import list_of_meetings

def main() -> None:


    for meeting in list_of_meetings:
        # if any variables are missing, raise an error
        if len(meeting) != 5:
            raise ValueError(f"\n\tError: Missing variables for meeting {meeting[0]}.")

    week = ClWeek()

    for meeting in list_of_meetings:
        week.import_meeting(meeting)

    # results are stored in a dictionary with each day name as key and the 'find_conflicts' return dict as a value.
    results = {day_name: week.days[day_name].find_conflicts() for day_name in list(week.days.keys())}

    # print(results)

if __name__ == "__main__":
    main()
