# Matthew Koch, Carolyn Grum, Beth Pearson


import matplotlib.pyplot as plt
from T040_M1_load_data import load_data as load_data
from T040_M1_load_data import add_average as add_avg
from T040_M2_student_list import student_list as sl


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
    student_list = sl(dictionary)

    # Create attribute dictionary
    attribute_dictionary = {}

    # Iterate through dictionary
    for student_info in student_list:

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

histogram(school_dictionary_with_avg, 'Health')
