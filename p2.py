"""
File: p2.py
Author: Ashraf Kawooya
Date: 11/18/2022
Lab Section: Section 11
Email:  ashrafk1@umbc.edu
Description:  This program displays particular commands for the attendance of students in a roster
                for a certain period of time
"""

# Comment the line below out if your have the load_dictionary function working!!
# Comment the line below out if your have the load_dictionary function working!!

from dataEntryP2 import fillAttendanceData

# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!


def print_list(xlist):
    """
       Simply prints the list. The function should not be able to change any
       values of that list passed in.
       :param xlist: the list in question
       :return: the information in the list
       """
    for element in xlist:
        print(element)


def connect_to_data_file(filename):
    # will return connection to data file
    infile = ''

    try:
        infile = open("rosters.txt", 'r')
        infile = open("dataAllShow1stClass.txt", "r")
        infile = open("dataAllShow1stAnd2ndClass.txt", "r")
        # infile = open(filename, "r")
    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file


def load_dictionary(attend_data):
    """
       Simply complies the data in the file into a dictionary.
       :param attend_data: contains the data of students that attended school
              for a given period for different days.
       :return: compiles the data into a dictionary
       """

    attend_dict = {}
    read_file = open(attend_data, 'r')
    for i in read_file:
        strip_data = i.strip()
        split_data = strip_data.split(',')
        names = ','. join(split_data[0:2])
        dates = ','.join((split_data[2:4]))
        if names not in attend_dict:
            attend_dict[names] = [dates]
        else:
            attend_dict[names] += [dates]
    return attend_dict


def is_present(student_name, date, attend_data):
    """
       Displays results whether a student attended class on a particular day.
       :param student_name: the particular person needed from the data file
       :param date: date for when the student might have attended or not
       :param attend_data: contains information regarding the attendance of the students
       :return: True or False for the particular student in question
       """
    if date in attend_data[student_name][0] or date in attend_data[student_name][1]:
        return True
    else:
        return False


def display_attendance_data_for_student(student_name, attend_data):
    """
       Display the log-in data for that particular student if present
       :param student_name: Name of the student in question
       :param attend_data: information regarding the log-in period for the students
       :return: the log-in info for a particular student if present or
                no student of this name in attendance log if absent
       """
    if student_name in attend_data:
        print(student_name, attend_data[student_name])
    else:
        print('No student of this name in the attendance log')


def list_all_students_checked_in(date, attend_data):
    """
       Displays all names of students that checked in on a certain day
       :param date: date in question for attendance
       :param attend_data: information regarding the log-in period for the students
       :return: names of students that attended on that particular day
       """
    student_name = []
    for key in attend_data:
        first_attendance = attend_data[key][0]
        second_attendance = attend_data[key][1]
        if date in first_attendance or date in second_attendance:
            student_name.append(key)
    return student_name


def list_all_students_checked_in_before(date, time, attend_data):
    """
       Displays students who attended before a particular time
       :param date: particular day required to get the time period of log-in
       :param time: particular time in question to get students that came before then
       :param attend_data: information regarding the log-in period for the students
       :return: names of students that came before that time
       """
    student_name = []

    period_hour = int(time[0:2]) * 3600
    period_min = int(time[3:5]) * 60
    period_sec = int(time[6:8])
    period = period_hour + period_min + period_sec

    for key in attend_data:
        first_attendance = attend_data[key][0]
        second_attendance = attend_data[key][1]

        first_hour = int(first_attendance[0:2]) * 3600
        first_min = int(first_attendance[3:5]) * 60
        first_sec = int(first_attendance[6:8])
        first_time = first_hour + first_min + first_sec

        second_hour = int(second_attendance[0:2]) * 3600
        second_min = int(second_attendance[3:5]) * 60
        second_sec = int(second_attendance[6:8])
        second_time = second_hour + second_min + second_sec

        if date in first_attendance or date in second_attendance:
            if first_time < period or second_time < period:
                student_name.append(key)

    for value in student_name:
        print(value)
    return student_name


def list_students_attendance_count(attend_data, times, student_ros):
    """
       Counts the number of students that attended school for particular number of classes
       :param attend_data: contains that info for attendance for the students
       :param times: number of times they attended class
       :param student_ros: contains the whole roster of students that are in the school
       :return: the names of students who attended for particular number of days and the
                number of students that attended
       """
    student_name = []
    not_attend = []
    for name in student_ros:
        if name in attend_data:
            if len(attend_data[name]) == times:
                student_name.append(name)
        elif name not in attend_data:
            not_attend.append(name)
    if times == 0:
        return not_attend
    return student_name


def print_dictionary(attend_data):
    """
       Simply prints the dictionary. The function should not be able to change any
       values of that dictionary passed in.
       :param attend_data: contains the data for the particular dictionary required to be printed
       :return: the dictionary in question
       """
    for i in attend_data:
        print(i, attend_data[i])


def get_student_to_first_enter(date, attend_data):
    """
       Displays the name of the first student to attend class on that day
       :param date: day in question required to produce results
       :param attend_data: information regarding the log-in period for the student
       :return: the names of students that attended first that day
       """
    student_name = []
    for key in attend_data:
        first_attendance = attend_data[key][0]
        second_attendance = attend_data[key][1]
        if date in first_attendance or date in second_attendance:
            student_name.append(key)
    return student_name[0]


def print_count(attend_data):
    """
       The number of items in a particular query
       :param attend_data: information regarding the log-in period for the student
       :return: the number in the list of students for a certain query
       """
    print(f'There were {len(attend_data)} records for this query')


def load_roster(roster_file_name):
    """
       Simply complies the data in the file into a list.
       :param roster_file_name: file in question that contains the data
       :return: compiles the data into a list
       """
    my_list = []
    roster_file = open(roster_file_name, 'r')
    for name in roster_file:
        roster_strip = name.strip()
        my_list.append(roster_strip)

    return my_list


if __name__ == '__main__':

    infile = connect_to_data_file('randomData.txt')
    if infile:
        print('connected to data file...')
    else:
        print('issue with data file... STOP')
        exit(1)

    # FIRST OBJECTIVE
    data = fillAttendanceData()
    # data = load_dictionary('dataAllShow1stAnd2ndClass.txt')
    print(data)

    roster = load_roster('rosters.txt')
    print(roster)

    # just making sure the data collected is good
    print_dictionary(data)

    print("********* Looking up Student Attendance Data ***********")
    display_attendance_data_for_student("Morrison, Simon", data)
    display_attendance_data_for_student("Arsenault, Al", data)

    print("********* Looking to see if Student was present on date ***********")
    print(is_present("Bower, Amy", "11/5/2022", data))
    print(is_present("Bower, Amy", "11/17/2022", data))

    # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/5/2022", data)
    print_list(result)
    print_count(result)

    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
    print_list(result)
    print_count(result)

    # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    result = list_students_attendance_count(data, 2, roster)
    print_list(result)
    print_count(result)

    # list the student that showed up for one day
    print("*** Those who attended ONE class")
    result = list_students_attendance_count(data, 1, roster)
    print_list(result)
    print_count(result)

    # list the student that showed up for no days
    print("*** Those who attended NO class")
    result = list_students_attendance_count(data, 0, roster)
    print_list(result)
    print_count(result)

    # print student to first enter
    print("**** First student to enter on 11/2/2022 ****")
    result = get_student_to_first_enter('11/2/2022', data)
    print(result)
    print("**** First student to enter on 11/3/2022 ****")
    result = get_student_to_first_enter('11/3/2022', data)
    print(result)
    print("**** First student to enter on 11/4/2022 ****")
    result = get_student_to_first_enter('11/4/2022', data)
    print(result)
    print("**** First student to enter on 11/5/2022 ****")
    result = get_student_to_first_enter('11/5/2022', data)
    print(result)


