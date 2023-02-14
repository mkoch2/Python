# Matthew Koch, Carolyn Grum, Beth Pearson

import numpy as np
import matplotlib.pyplot as plt
from T040_M1_load_data import load_data as load_data
from T040_M1_load_data import add_average as add_avg
from T040_M2_student_list import student_list as sl


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

    student_list = sl(dictionary)

    # Create attribute dictionary
    attribute_dictionary = {}

    # Iterate through student_list
    for student_info in student_list:

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

    # Selection sort of list of x-values
    # Traverse through all array elements
    for i in range(len(x)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(x)):
            if x[min_idx] > x[j]:
                min_idx = j
                # Swap the found minimum element with
                # the element in position i
        x[i], x[min_idx] = x[min_idx], x[i]

    # Returns list of coefficients and interval of x
    my_tuple = (z, [x[0], x[-1]])
    return my_tuple


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


# Main

my_tuple = curve_fit(school_dictionary_with_avg, 'Health', 2)
print(my_tuple)

