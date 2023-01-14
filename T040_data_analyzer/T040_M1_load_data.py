# Matthew Koch, Carolyn Grum, Beth Pearson

import string
from typing import List
from check_equal import check_equal as check

from T040_TM1_1 import test_load_data_keys as test_keys
from T040_TM1_2 import test_dictionary_values_size_of_lists as test_lists_size
from T040_TM1_3 import test_load_data_student_entries as test_entries
from T040_TM1_4 import test_add_average as test_avg


# ------------------------------Function 1--------------------------------------


def student_school_dictionary(file_name: str) -> dict:
    r"""returns a dictionary where the keys are the initials of the schools the students attended, given a filename

    Preconditions: None

    Examples:

    >>>student_school_dictionary(r'C:\Users\matth\Downloads\student-mat.csv')
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },...]}

    """
    student_school = {}
    student_type = 'School'

    # Open Spreadsheet
    infile = open(file_name, 'r')

    # Skips first line in spreadsheet
    found_keys = False

    # Reads one line at a time
    for line in infile:
        good_data = [''] * 9
        data = line.split(',')

        # Removing extra white space
        index = 0
        for string in data:
            good_data[index] = string.strip()

            index += 1

        # Remove new line character
        good_data[8] = good_data[8].replace('\n', '')

        # Setting up keys ex: school, age, studytime, etc
        if found_keys == False:
            keys = good_data
            found_keys = True

        else:
            # Add student info into school dictionary, involves 3 steps:

            # Step 1: Build my student_info dictionary
            # Example {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, ...}

            # Resetting student_info dictionary
            student_info = {}
            index = 0

            # For each key, assign dictionary value from spreadsheet line (good_data)
            for key in keys:

                # Don't need to add school code
                # ex: GP, MB, CF
                if key != student_type:
                    # Updates student_info dictionary with one key value
                    # Ex: Age: 18, or StudyTime: 2
                    student_info.update({key: int(good_data[index])})

                # Move to next key
                index += 1

            # Step 2: Add completed student_info dictionary into list

            # Get list from student_school dictionary (good_data[0])
            school_list = student_school.get(good_data[0])

            # If first time adding to specific school code, create new list
            if school_list == None:
                newList = []
                # Add school_info into list
                newList.append(student_info)

                # Step 3: Add new list to student_school dictionary at specific school code
                student_school.update({good_data[0]: newList})

            else:
                # If list is already found at specific school code, append to list
                # Even though put in to school dictionary as 'newList', this is not its name. It has no name. To get list use .get() and assign variable name
                school_list.append(student_info)

    # Close file
    infile.close()

    # Return full dictionary
    return student_school

# ------------------------------Function 2--------------------------------------


def student_health_dictionary(file_name: str) -> dict:
    r"""returns a dictionary where the keys are the students' health numbers,
    given a filename

    Preconditions: good_data[4] >=1 and good_data[4] <= 5

    Examples:

    >>>student_health_dictionary(r'C:\Users\matth\Downloads\student-mat.csv')
    { 1 : [ {'School':'GP', 'Age': 17, 'StudyTime': 4.2, 'Failures': 3,
'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10 },...]}

    """

    student_health = {}
    student_type = 'Health'

    # Open spread sheet
    infile = open(file_name, 'r')

    foundkeys = False

    for line in infile:

        good_data = [''] * 9
        data = line.split(',')

        # Removing extra white space
        index = 0
        for string in data:
            good_data[index] = string.strip()

            index += 1

        # Remove new line character
        good_data[8] = good_data[8].replace('\n', '')

        if foundkeys == False:
            keys = good_data
            foundkeys = True

        else:

            # Resetting student_info dictionary
            student_info = {}
            index = 0

            for key in keys:
                if key != student_type:

                    if key == 'School':
                        student_info.update({key: good_data[index]})

                    else:
                        student_info.update({key: int(good_data[index])})

                index += 1

            # Step 2: Add completed student_info dictionary into list

            # Get list from student_health dictionary (good_data[4])
            health_list = student_health.get(int(good_data[4]))

            # If first time adding to specific school code, create new list
            if health_list == None:
                newList = []

                newList.append(student_info)

                # Step 3: Add new list to student_health dictionary at specific school code
                student_health.update({int(good_data[4]): newList})

            else:

                health_list.append(student_info)

    # Close file
    infile.close()

    # Return full dictionary
    return student_health

# ------------------------------Function 3--------------------------------------


def student_age_dictionary(file_name: str) -> dict:
    r""" Create a dictionary where the keys are the students ages, ranging from
    lowest to highest.

    Preconditions: Age ranges from 15 to 22

    >>>student_age_dictionary(r'C:\Users\cgdoo\Pictures\Code\student-mat.csv')

        { 15 : [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3,

        'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}, … ],



       16 : [ {'School': 'MS', 'StudyTime': 1, 'Failures': 1.2, 'Health': 4,

       'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7}, {another element}, … ],


    >>>student_age[15]

        { 15 : [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3,

        'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}, … ],


    >>>student_age[22]

        { 22 : [ {'School': 'BD', 'StudyTime': 1, 'Failures': 3, 'Health': 1,

        'Absences': 16, 'G1': 6, 'G2': 8, 'G3': 8}]

    """

    student_age = {}
    student_type = 'Age'

    infile = open(file_name, 'r')  # Open the spreadsheet

    found_keys = False  # Skips first line in spreadsheet

    for line in infile:  # Reads one line at a time
        good_data = [''] * 9
        data = line.split(',')

        index = 0  # Removes extra white space

        for string in data:
            good_data[index] = string.strip()
            index += 1

        good_data[8] = good_data[8].replace(
            '\n', '')  # Remove new line character

        if found_keys == False:  # Setting up keys ex: school, age, studytime, etc
            keys = good_data
            found_keys = True

        else:
            # Add student info into school dictionary, involves 3 steps:
            # Step 1: Build my student_info dictionary
            # Example {'School': 'GP', 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, ...}
            # Resetting student_info dictionary
            student_info = {}
            index = 0

            # For each key, assign dictionary value from spreadsheet line (good_data)
            for key in keys:
                if key == 'School':
                    student_info.update({key: good_data[index]})

                else:
                    student_info.update({key: int(good_data[index])})

                index += 1  # Move to next key

            # Step 2: Add completed student_info dictionary into list
            # Get list from student_age_dictionary (good_data[1])
            age_list = student_age.get(int(good_data[1]))

            # If first time adding to specific age code, create new list
            if age_list == None:
                newList = []

                # Add age_info into list
                newList.append(student_info)

                # Step 3: Add new list to student_age_dictionary at specific age code
                student_age.update({int(good_data[1]): newList})

            else:
                # If list is already found at specific age code, append to list
                # Even though put in to school dictionary as 'newList', this is not its name. It has no name. To get list use .get() and assign variable name

                age_list.append(student_info)

    # Close file
    infile.close()

    # Return full dictionary, sorted from lowest to highest
    return student_age

# ------------------------------Function 4--------------------------------------


def student_failures_dictionary(file_name: str) -> dict:
    r"""returns a dictionary where the keys are the students' health numbers,
    given a filename

    Preconditions: good_data[3] >= 0 and good_data[3] <= 10

    Examples:

    >>>student_failures_dictionary(r'C:\Users\matth\Downloads\student-mat.csv')
    { 0 : [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3,
 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},...]}

    """

    student_failures = {}
    student_type = 'Failures'

    # Open spread sheet
    infile = open(file_name, 'r')

    foundkeys = False

    for line in infile:

        good_data = [''] * 9
        data = line.split(',')

        # Removing extra white space
        index = 0
        for string in data:
            good_data[index] = string.strip()

            index += 1

        # Remove new line character
        good_data[8] = good_data[8].replace('\n', '')

        if foundkeys == False:
            keys = good_data
            foundkeys = True

        else:

            # Resetting student_info dictionary
            student_info = {}
            index = 0

            for key in keys:
                if key != student_type:
                    # Updates student_info dictionary with one key value
                    # Ex: Age: 18, or StudyTime: 2
                    if key == 'School':
                        student_info.update({key: good_data[index]})

                    else:
                        student_info.update({key: int(good_data[index])})

                # Move to next key
                index += 1

            # Step 2: Add completed student_info dictionary into list

            failure_list = student_failures.get(int(good_data[3]))

            # If first time adding to specific school failure, create new list
            if failure_list == None:
                newList = []
                # Add school_info into list
                newList.append(student_info)

                # Step 3: Add new list to student_health dictionary at specific school code
                student_failures.update({int(good_data[3]): newList})

            else:
                # If list is already found at specific health, append to list
                # Even though put in to school dictionary as 'newList', this is not its name. It has no name. To get list use .get() and assign variable name
                failure_list.append(student_info)

    # Close file
    infile.close()

    # Return full dictionary
    return student_failures

# ------------------------------Load Data---------------------------------------


def load_data(file_name: str, sort_type_dictionary: str) -> dict:
    r"""returns a dictionary of data in the way that the user specifies,
    given a filename and dictionary key ('School', 'Age', 'Health', 'Failures')

    Preconditions: None

    Examples:
    >>>load_data(r'C:\Users\matth\Downloads\student-mat.csv','School')
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },...]}

    >>>load_data(r'C:\Users\matth\Downloads\student-mat.csv','Failures')
    { 0 : [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3,
 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},...]}

    >>>load_data(r'C:\Users\matth\Downloads\student-mat.csv','Gender')
    Invalid key
    {}

    """

    if sort_type_dictionary == 'School':
        return student_school_dictionary(file_name)

    elif sort_type_dictionary == 'Age':
        return student_age_dictionary(file_name)

    elif sort_type_dictionary == 'Health':
        return student_health_dictionary(file_name)

    elif sort_type_dictionary == 'Failures':
        return student_failures_dictionary(file_name)

    else:
        print('Invalid key')
        return {}

# ------------------------------Add Average-------------------------------------


def add_average(dictionary: dict) -> dict:
    r"""returns the dictionary updated with the average grade of the student grades,
    given a dictionary

    Preconditions: avg_grade >= 0

    Examples:
    >>>{ 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },...]}

    """
    # Iterate dictionary keys
    for key in dictionary.keys():
        # Get values at the key (list)
        student_info_list = dictionary.get(key)
        # Iterate through list at the key
        for student_info in student_info_list:
            # Get three grades and average
            grade_1 = student_info.get('G1')
            grade_2 = student_info.get('G2')
            grade_3 = student_info.get('G3')
            avg_grade = format(((grade_1 + grade_2 + grade_3) / 3), '.2f')

            # Update student_info dictionary
            # Format 2 decimal places
            student_info.update({'G_Avg': avg_grade})

    return dictionary


# Test Data

# Dicitonaries:
# student_school_dictionary(r'C:\Users\matth\Downloads\student-mat.csv')
# student_health_dictionary(r'C:\Users\matth\Downloads\student-mat.csv')
# student_age_dictionary(r'C:\Users\matth\Downloads\student-mat.csv')
# student_failures_dictionary(r'C:\Users\matth\Downloads\student-mat.csv')


# Load Data Call
# load_data(r'C:\Users\matth\Downloads\student-mat.csv','School')

# Add Average Call
# add_average(student_school_dictionary(r'C:\Users\matth\Downloads\student-mat.csv'))


# Create Dicitonaries
school_dictionary = load_data(
    r'C:\Users\matth\Downloads\student-mat.csv', 'School')
health_dictionary = load_data(
    r'C:\Users\matth\Downloads\student-mat.csv', 'Health')
age_dictionary = load_data(
    r'C:\Users\matth\Downloads\student-mat.csv', 'Age')
failures_dictionary = load_data(
    r'C:\Users\matth\Downloads\student-mat.csv', 'Failures')


total_tests_passed = 0
total_tests_failed = 0

dictionary_types = {'School': school_dictionary,
                    'Health': health_dictionary,
                    'Age': age_dictionary,
                    'Failures': failures_dictionary}

# Test 1: Dictionary Keys

for dict_type in dictionary_types:

    tests_passed, tests_failed = test_keys(
        dictionary_types.get(dict_type), dict_type)

    total_tests_passed += tests_passed
    total_tests_failed += tests_failed


# Test 2: Dictionary Values: Size of the Lists

for dict_type in dictionary_types:

    tests_passed, tests_failed = test_lists_size(
        dictionary_types.get(dict_type), dict_type)

    total_tests_passed += tests_passed
    total_tests_failed += tests_failed


# Test 3: Dictionary Values: Individual Student Entries

for dict_type in dictionary_types:

    tests_passed, tests_failed = test_entries(
        dictionary_types.get(dict_type), dict_type)

    total_tests_passed += tests_passed
    total_tests_failed += tests_failed


# Test 4: Add Average

# Add average dictionaries

school_dictionary_with_avg = add_average(school_dictionary)
health_dictionary_with_avg = add_average(health_dictionary)
age_dictionary_with_avg = add_average(age_dictionary)
failures_dictionary_with_avg = add_average(failures_dictionary)

dictionary_types_with_avg = {'School': school_dictionary_with_avg,
                             'Health': health_dictionary_with_avg,
                             'Age': age_dictionary_with_avg,
                             'Failures': failures_dictionary_with_avg}

for dict_type in dictionary_types:

    tests_passed, tests_failed = test_avg(
        dictionary_types.get(dict_type),
        dictionary_types_with_avg.get(dict_type))

    total_tests_passed += tests_passed
    total_tests_failed += tests_failed

# Print All tests
print('Total Tests passed: ', total_tests_passed)
print('Total Tests failed: ', total_tests_failed)

