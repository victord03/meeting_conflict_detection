# Meeting Conflict Detection

A Python tool for detecting scheduling conflicts in weekly meeting calendars. Identifies both time slot overlaps and participant double-booking across a 5-day work week.

## Features

- **Time Slot Conflict Detection**: Identifies overlapping meetings in the same time slots
- **Participant Double-Booking**: Detects when individuals are scheduled for multiple meetings simultaneously
- **30-Minute Slot Granularity**: Tracks meetings in half-hour increments (9:00 AM - 6:30 PM)
- **Weekly Calendar View**: Manages Monday through Friday scheduling
- **Clean OOP Design**: Uses dataclasses for day and week management

## How It Works

The tool uses a time slot dictionary system where each half-hour is represented as a float (9.0, 9.5, 10.0, etc.). Conflicts are detected using set operations to find:
1. Meetings scheduled in the same time slots
2. Project managers or participants assigned to multiple meetings at once

## Installation

```bash
# Clone the repository
git clone https://github.com/victord03/meeting_conflict_detection.git
cd meeting_conflict_detection

# No external dependencies required (uses Python stdlib)
python3 src/main.py
```

## Usage

Define your meetings in `src/main.py`:

```python
# Define participants
pm3 = "Kakamanis Victor"
pm2 = "{PM Name}"

# Define meeting (name, start_time, duration, participants)
meeting = [
    "Project Kickoff",
    9.5,  # 9:30 AM
    1.0,  # 1 hour duration
    [pm1, pm2]
]

# Add to calendar
week = ClWeek()
week.add_meeting_on_day("Monday", meeting)

# Check for conflicts
conflicts = week.find_conflicts()
```

Run the detection:

```bash
python3 src/main.py
```

## Project Structure

```
meeting_conflict_detection/
├── classes/
│   ├── ClDay.py       # Day container with 30-min time slots
│   └── ClWeek.py      # Week container managing 5 days
├── src/
│   └── main.py        # Conflict checking
├── test/
│   └── test_main.py   # Test suite
└── README.md
```

## Tech Stack

- **Language**: Python 3.10+
- **Development**: Test-Driven Development (TDD)
- **Testing**: pytest
- **Code Style**: Black formatter

## Example Output

```
=== Conflicts Detected ===

Time Slot Conflicts:
- Monday 10:00-11:00: "Project Review" overlaps with "Team Standup"

Participant Double-Booking:
- Kaklamanis Victor: Double-booked on Tuesday 14:00-15:00 (Meeting X & Meeting Y)
```

## Development

Built using Test-Driven Development principles with 15 commits showing iterative refinement. The codebase demonstrates:
- Type validation with meaningful ValueErrors
- Set operations for efficient conflict detection
- Clean separation of concerns
- Proper documentation

## Status

**Functional MVP** - Core conflict detection working. Suitable for scheduling validation in professional environments.

## License

MIT License
