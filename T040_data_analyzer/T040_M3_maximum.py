# Matthew Koch, Carolyn Grum, Beth Pearson


import matplotlib.pyplot as plt
from T040_M1_load_data import load_data as load_data
from T040_M1_load_data import add_average as add_avg
from T040_M2_student_list import student_list as sl
from T040_M2_curve_fit import curve_fit as cf
from scipy.optimize import fminbound


coef_list = []


def curve_function(x):
    coefficient_index = len(coef_list) - 1
    curve_result = 0
    for coefficient in coef_list:
        curve_result += coefficient * x ** coefficient_index
        coefficient_index -= 1
    return -curve_result


def maximum(attribute: str) -> tuple:
    """"Returns a tuple containing the x and y value of the local maximum
    between the lowest and highest value of the attribute,
    given an attribute

    Precondtitions: None

    Examples:
    >>>local_max_coord = maximum('Health')
    (1.000005628673589, 11.850596436418066)
    >>>local_max_coord = maximum('Failures')
    (2.9999965472915386, 286.35546183545836)
    >>>local_max_coord = maximum('Age')
    (21.99999391225472, 9498864622.67594)
    """

    curve_fit = cf(school_dictionary_with_avg, attribute, 2)

    for i in curve_fit[0]:
        coef_list.append(i)

    curve_interval = curve_fit[1]

    x1 = curve_interval[0]
    x2 = curve_interval[1]

    x_max = fminbound(curve_function, x1, x2)

    y_max = curve_function(x_max)

    local_max_coord = (x_max, y_max * -1)

    return local_max_coord


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

'''
local_max_coord = maximum('Health')
print(local_max_coord)
local_max_coord = maximum('Failures')
print(local_max_coord)
local_max_coord = maximum('Age')
print(local_max_coord)
'''
