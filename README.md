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

The tool requires two data files in the `data/` folder (not tracked in git for privacy):

1. **data/pm_names.py** - Defines project manager/participant names
2. **data/meeting_names.py** - Defines meeting schedules

See the [Data Structure](#data-structure) section below for format details.

Run the detection:

```bash
python3 src/main.py
```

## Project Structure

```
meeting_conflict_detection/
├── classes/
│   ├── ClDay.py           # Day container with 30-min time slots
│   └── ClWeek.py          # Week container managing 5 days
├── data/                  # Not tracked in git (contains sensitive data)
│   ├── pm_names.py        # Participant names
│   └── meeting_names.py   # Meeting schedules
├── src/
│   └── main.py            # Conflict checking logic
├── test/
│   └── test_main.py       # Test suite
└── README.md
```

## Data Structure

To use this tool, create a `data/` folder with two Python files:

### data/pm_names.py

Define participant names as simple string variables:

```python
"""Participant names for meeting conflict detection"""

pm1 = "John Smith"
pm2 = "Jane Doe"
pm3 = "Alice Johnson"
pmo = "Bob Wilson"
```

### data/meeting_names.py

Import the participant names and define meetings as a list of 5-element lists:

```python
"""Meeting schedules for conflict detection"""

from data.pm_names import pm1, pm2, pm3, pmo

# Meeting format: [name, start_time, duration, participant, day]
# start_time: float (9.0 = 9:00 AM, 9.5 = 9:30 AM, 14.0 = 2:00 PM)
# duration: float in hours (0.5 = 30min, 1.0 = 1hr, 1.5 = 90min)
# day: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"

list_of_meetings = [
    ["Project Kickoff", 9.5, 1.0, pm1, "Monday"],
    ["Team Standup", 10.0, 0.5, pm2, "Monday"],
    ["Client Review", 14.0, 1.5, pm3, "Tuesday"],
    ["PMO Sync", 11.0, 0.5, pmo, "Wednesday"],
    # Add more meetings here...
]
```

**Note:** The `data/` folder is gitignored to keep sensitive colleague names and meeting details private.

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
- John Smith: Double-booked on Tuesday 14:00-15:00 (Meeting X & Meeting Y)
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
