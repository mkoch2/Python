# Matthew Koch, Carolyn Grum, Beth Pearson


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
    return curve_result


def minimum(attribute: str) -> tuple:
    """"Returns a tuple containing the x and y value of the local minimum
    between the lowest and highest value of the attribute,
    given an attribute

    Precondtitions: None

    Examples:
    >>>local_min_coord = minimum('Health')
    (3.688182638901082, 10.266627057271565)
    >>>local_min_coord = minimum('Failures')
    (0.25838764494397626, 10.896219116726654)
    >>>local_min_coord = minimum('Age')
    (15.00000608774528, 436593602.75415564)
    """

    curve_fit = cf(school_dictionary_with_avg, attribute, 2)

    for i in curve_fit[0]:
        coef_list.append(i)

    curve_interval = curve_fit[1]

    x1 = curve_interval[0]
    x2 = curve_interval[1]

    x_min = fminbound(curve_function, x1, x2)

    y_min = curve_function(x_min)

    local_min_coord = (x_min, y_min)

    return local_min_coord


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
local_min_coord = minimum('Health')
print(local_min_coord)
local_min_coord = minimum('Failures')
print(local_min_coord)
local_min_coord = minimum('Age')
print(local_min_coord)'''

