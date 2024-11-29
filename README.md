
# Student Attendance System

## Overview
This project is a Python-based attendance system that processes and analyzes student attendance data. It allows querying attendance records, listing attendance details for specific dates, and performing various operations such as counting attendance frequency and identifying students who attended on specific days or times.

## Features

### Attendance Data Handling
- **Fill Attendance Data**:
  - Predefined attendance data for testing purposes.
  - Option to load data from external files.
- **Data Storage**:
  - Attendance data stored in dictionaries for easy manipulation.
  - Roster data stored in lists.

### Attendance Queries
- Check if a student attended on a specific date.
- Display attendance details for an individual student.
- List all students who attended on a specific date or before a given time.
- Identify the first student to check in on a specific date.

### Reporting
- Count the total number of attendance records.
- List students who attended:
  - All classes.
  - Some classes.
  - No classes.

### Utility Functions
- Print attendance data in dictionary or list formats.
- Load roster data from files.

## Files

### Source Files
1. **`dataEntryP2.py`**:
   - Contains predefined attendance data for testing.
   - Provides the `fillAttendanceData` function to initialize data.

2. **`p2.py`**:
   - Implements the main program logic.
   - Provides functions for attendance queries, reporting, and data manipulation.

### Data Files
- Attendance and roster data files (e.g., `rosters.txt`, `dataAllShow1stAnd2ndClass.txt`) for input.

## Installation

1. Clone or download the repository to your local machine.
2. Ensure Python 3.x is installed on your system.

## Usage

1. Run the program:
   ```bash
   python3 p2.py
   ```
2. Follow the prompts to execute specific queries or view reports.

## Functionality Examples

### Check Attendance
```python
# Check if a student attended on a specific date
is_present("Bower, Amy", "11/5/2022", data)
```

### Display Attendance Data for a Student
```python
# Display log-in information for a specific student
display_attendance_data_for_student("Morrison, Simon", data)
```

### List Students by Attendance
```python
# List students who attended before a specific time on a given date
list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
```

### Identify First Check-In
```python
# Find the first student to check in on a specific date
get_student_to_first_enter("11/2/2022", data)
```

## Dependencies
- Python 3.x
- External data files (optional, for extended functionality).

## Authors
- **Ashraf Kawooya**
- **Date**: 11/18/2022
- **Email**: ashrafk1@umbc.edu

## License
This project is for educational purposes and is distributed as-is.
