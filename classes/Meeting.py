from multiprocessing.managers import Value


class Meeting:
    name: str
    day: str
    meet_time: float
    duration: float
    owner: str
    occurrence: str

    def __init__(self, name, day, meet_time, duration, owner, occurrence=None):

        if type(name) != str:
            raise ValueError

        if type(day) != str:
            raise ValueError

        if type(meet_time) != float:
            raise ValueError

        if type(duration) != float:
            raise ValueError

        if type(owner) != str:
            raise ValueError

        self.name = name
        self.day = day
        self.meet_time = meet_time
        self.duration = duration
        self.owner = owner
        self.occurrence = occurrence

    def __str__(self):
        return f'Meeting name: {self.name}\nDay: {self.day}\nTime: {self.meet_time}'
