# Matthew Koch, Carolyn Grum, Beth Pearson

import numpy as np
import matplotlib.pyplot as plt
from T040_M1_load_data import load_data as load_data
from T040_M1_load_data import add_average as add_avg
from T040_M2_student_list import student_list as sl


def student_list(dictionary: dict) -> list:
    """returns a dictionary as a list, 
    given a dictionary

    Preconditions: None 

    Examples:
    >>>
    """
    result_list = []
    keys = dictionary.keys()
    for key in keys:
        key_list = dictionary.get(key)

        for student_info in key_list:
            if student_info.get('School') == None:
                student_info.update({'School': key})
            elif student_info.get('Health') == None:
                student_info.update({'Health': key})
            elif student_info.get('Age') == None:
                student_info.update({'Age': key})
            elif student_info.get('Failures') == None:
                student_info.update({'Failures': key})

            result_list.append(student_info)

    return result_list


def sort_students_bubble(dictionary: dict, attribute: str) -> list:
    """ Returns a sorted list of the students by the attribute inputted

    Precondition: Value assigned to the key can be string, int, or float

    Examples:
    >>>sort_students_bubble(failures_dictionary_with_avg, 'School')
    [{'School': 'BD', 'Age': 17, 'StudyTime': 2, 'Health': 5, 'Absences': 14,
    'G1': 12, 'G2': 12, 'G3': 12, 'G_Avg': '12.00', 'Failures': 0}, ...

    {'School': 'MS', 'Age': 18, 'StudyTime': 2, 'Health': 5, 'Absences': 0,
    'G1': 6, 'G2': 5, 'G3': 0, 'G_Avg': '3.67', 'Failures': 1}]

    >>>sort_students_bubble(failures_dictionary_with_avg, 'G1')
    [{'School': 'BD', 'Age': 18, 'StudyTime': 2, 'Health': 5, 'Absences': 8,
    'G1': 3, 'G2': 5, 'G3': 5, 'G_Avg': '4.33', 'Failures': 1}, ...

    {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Health': 1, 'Absences': 0,
    'G1': 19, 'G2': 18, 'G3': 19, 'G_Avg': '18.67', 'Failures': 0}]

    >>> sort_students_bubble(failures_dictionary_with_avg, 'G_Avg')
    [{'School': 'MB', 'Age': 16, 'StudyTime': 1, 'Health': 5, 'Absences': 0,
    'G1': 4, 'G2': 0, 'G3': 0, 'G_Avg': '1.33', 'Failures': 2}, ...

    {'School': 'GP', 'Age': 15, 'StudyTime': 1, 'Health': 5, 'Absences': 0,
    'G1': 8, 'G2': 10, 'G3': 11, 'G_Avg': '9.67', 'Failures': 0}]
    """

    # list generated from student_list function
    list1 = student_list(dictionary)

    if attribute != 'School':
        swap = True
        while swap:
            swap = False
            for i in range(len(list1) - 1):  # sets range to number of elements in list1
                # checks if attribute is int/float
                if type(list1[i].get(attribute)) is int or type(list1[i].get(attribute)) is float:
                    # checks to see if next element in list1 is less than one before
                    if float(list1[i].get(attribute)) > float(list1[i + 1].get(attribute)):
                        swap = True  # if next elements is less, it gets swapped with previous element
                # checks if attribute is string ('School')
                elif type(list1[i].get(attribute)) is str:
                    # converts value associated with School key into lowercase so it can be given a value and compares size
                    if float(list1[i].get(attribute).lower()) > float(list1[i + 1].get(attribute).lower()):
                        swap = True  # if next element in list is less, it gets swapped with previous element

                if swap:
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]  # swap

        return list1  # return sorted list

    if attribute == 'School':
        swap = True
        while swap:
            swap = False
            for i in range(len(list1) - 1):  # sets range to number of elements in list1
                # checks if attribute is int/float
                if type(list1[i].get(attribute)) is int or type(list1[i].get(attribute)) is float:
                    # checks to see if next element in list1 is less than one before
                    if (list1[i].get(attribute)) > (list1[i + 1].get(attribute)):
                        swap = True  # if next elements is less, it gets swapped with previous element
                # checks if attribute is string ('School')
                elif type(list1[i].get(attribute)) is str:
                    # converts value associated with School key into lowercase so it can be given a value and compares size
                    if (list1[i].get(attribute).lower()) > (list1[i + 1].get(attribute).lower()):
                        swap = True  # if next element in list is less, it gets swapped with previous element

                if swap:
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]  # swap

        return list1  # return sorted list


list2 = []  # Empty List to update at end (For selection sort)


def sort_students_selection(dictionary: dict, attribute: str) -> list:
    """ Function takes two inputs, a dictionary and an attribute, and 
    outputs a list sorted, using selection sort, by the indicated attribute

    Precondition: Key values are string, int, or float

    >>>sort_students_selection(failures_dictionary_with_avg, 'School')
    [{'School': 'BD', 'Age': 17, 'StudyTime': 2, 'Health': 5, 'Absences': 14,
    'G1': 12, 'G2': 12, 'G3': 12, 'G_Avg': '12.00', 'Failures': 0}, ... 

    {'School': 'MS', 'Age': 18, 'StudyTime': 2, 'Health': 5, 'Absences': 0,
    'G1': 6, 'G2': 5, 'G3': 0, 'G_Avg': '3.67', 'Failures': 1}]

    >>>sort_students_selection(failures_dictionary_with_avg, 'G1')
    [{'School': 'BD', 'Age': 18, 'StudyTime': 2, 'Health': 5, 'Absences': 8,
    'G1': 3, 'G2': 5, 'G3': 5, 'G_Avg': '4.33', 'Failures': 1}, ...

    {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Health': 1, 'Absences': 0,
    'G1': 19, 'G2': 18, 'G3': 19, 'G_Avg': '18.67', 'Failures': 0}]

    >>> sort_students_selection(failures_dictionary_with_avg, 'G_Avg')
    [{'School': 'MB', 'Age': 16, 'StudyTime': 1, 'Health': 5, 'Absences': 0,
    'G1': 4, 'G2': 0, 'G3': 0, 'G_Avg': '1.33', 'Failures': 2}, ...

    {'Age': 16, 'StudyTime': 4, 'Failures': 0, 'Health': 2, 'Absences': 4,
    'G1': 19, 'G2': 19, 'G3': 20, 'G_Avg': '19.33', 'School': 'GP'}]
    """

    # list generated from student_list function
    list1 = student_list(dictionary)

    if attribute != 'School':
        for i in range(len(list1)):  # Set the index
            min_idx = i  # Minimum Index is set
            for j in range(i + 1, len(list1)):  # Next index to look at
                # If the attribute of min_idx is greater than the attribute of next index
                if float(list1[min_idx][attribute]) > float(list1[j][attribute]):
                    min_idx = j  # set min_idx to j
            # switch order of list
            list1[i], list1[min_idx] = list1[min_idx], list1[i]

            list2.append(list1[i])  # append the new order to list
        return list2  # returns the sorted list

    elif attribute == 'School':
        for i in range(len(list1)):  # Set the index
            min_idx = i  # Minimum Index is set
            for j in range(i + 1, len(list1)):  # Next index to look at
                # If the attribute of min_idx is greater than the attribute of next index
                if list1[min_idx][attribute] > list1[j][attribute]:
                    min_idx = j  # set min_idx to j
            # switch order of list
            list1[i], list1[min_idx] = list1[min_idx], list1[i]

            list2.append(list1[i])  # append the new order to list
        return list2  # returns the sorted list


def curve_fit(dictionary: dict, attribute: str, degree_of_polynomial: int) -> list:
    """returns the equation of the best fit as a list of coefficents, 
    given a dictionary, grade indicator, and degree of polynomial to be fitted to the data

    Preconditions: 1 <= degree_of_polynomial <= 5

    Examples:
    >>>curve_fit(school_dictionary_with_avg, 'Health', 4)
    [-0.03594956  0.40354081 -1.31219096  0.65310616 12.16319567]
    >>>curve_fit(school_dictionary_with_avg, 'Failures', 2)
    [ 0.35420697 -2.72986779 11.35634309]
    >>>curve_fit(school_dictionary_with_avg, 'Absences', 1)
    [-0.03061899 11.43300991]

    """

    list_of_students = student_list(dictionary)

    # Create attribute dictionary
    attribute_dictionary = {}

    # Iterate through list_of_students
    for student_info in list_of_students:

        # Retrieve student info
        # Get attribute value
        # ex: Health: 3
        attribute_value = student_info.get(attribute)

        # If attribute value is not a key Create a key with empty list
        avg_list = attribute_dictionary.get(attribute_value)

        if avg_list == None:
            new_avg_list = []
            new_avg_list.append(float(student_info.get('G_Avg')))
            attribute_dictionary.update({attribute_value: new_avg_list})

        # else add avg value into list
        else:
            avg_list.append(float(student_info.get('G_Avg')))

    # End of loop, attribute dictionary has all g_avg values

    # Create dictionary with avg of g_avgs
    dictionary_with_avg = {}

    # Iterate through attribute dictionary
    for attribute_value in attribute_dictionary:

        # For each key, get list
        avg_list = attribute_dictionary.get(attribute_value)

        # Iterate through list
        # Calculate avg value of g_avgs
        total_avg = 0
        for avg in avg_list:
            total_avg += avg

        attribute_avg = total_avg / len(avg_list)

        # Update dicitonary with avg with key and its average
        dictionary_with_avg.update({attribute_value: attribute_avg})

    # Data points
    x = list(dictionary_with_avg.keys())
    y = list(dictionary_with_avg.values())

    max_order = len(x) - 1

    if degree_of_polynomial > max_order:
        degree_of_polynomial = max_order

    # List of coeffients of line of best fit
    z = list(np.polyfit(x, y, degree_of_polynomial))

    # Plotting
    #x_e = np.linspace(0, 5, 100)
    #y_e = np.polyval(z, x_e)
    #plt.plot(x, y, 'o', x_e, y_e, '-')
    # plt.show()

    return z


def histogram(dictionary: dict, attribute: str) -> bool:
    """returns None and plots and show a histogram,
    given a dictionary and an attribute

    Preconditions:

    Examples:
    >>>histogram(school_dictionary_with_avg, 'Age')
    None
    >>>histogram(school_dictionary_with_avg, 'G_Avg')
    None
    >>>histogram(school_dictionary_with_avg, 'School')
    None

    """
    list_of_students = student_list(dictionary)

    # Create attribute dictionary
    attribute_dictionary = {}

    # Iterate through dictionary
    for student_info in list_of_students:

        # Retrieve attribute value
        attribute_value = student_info.get(attribute)

        attribute_list = attribute_dictionary.get(attribute_value)

        # If attribute value is not a key in attribute dictionary, create new list
        if attribute_list == None:
            new_attribute_list = []
            new_attribute_list.append(student_info)
            attribute_dictionary.update(
                {attribute_value: new_attribute_list})

        # adds student_info to attribute list
        else:
            attribute_list.append(student_info)

    # End of loop, attribute dictionary has all students with attribute levels

    # Create dictionary with students
    dictionary_with_students = {}

    # Iterate through attribute_dictionary
    for attribute_value in attribute_dictionary:

        # Retrieve list of students
        list_of_students = attribute_dictionary.get(attribute_value)

        # Number of students at attribute level
        num_students = len(list_of_students)

        # Update dictionary_with_students
        dictionary_with_students.update({attribute_value: num_students})

    histogram = plt.figure()
    plt.title("Histogram")
    plt.xlabel(attribute)
    plt.ylabel('Number of Students')
    x = list(dictionary_with_students.keys())
    y = list(dictionary_with_students.values())
    plt.bar(x, y, color='red')
    plt.show()

    return None


# Create Dicitonaries
school_dictionary = load_data(
    r'C:\Users\matth\Downloads\student-mat.csv', 'School')
health_dictionary = load_data(
    r'C:\Users\matth\Downloads\student-mat.csv', 'Health')
age_dictionary = load_data(
    r'C:\Users\matth\Downloads\student-mat.csv', 'Age')
failures_dictionary = load_data(
    r'C:\Users\matth\Downloads\student-mat.csv', 'Failures')

# Add average dictionaries

school_dictionary_with_avg = add_avg(school_dictionary)
health_dictionary_with_avg = add_avg(health_dictionary)
age_dictionary_with_avg = add_avg(age_dictionary)
failures_dictionary_with_avg = add_avg(failures_dictionary)


# Main Call
'''
z = curve_fit(school_dictionary_with_avg, 'Health', 2)
print(z)
histogram(school_dictionary_with_avg, 'Health')'''
