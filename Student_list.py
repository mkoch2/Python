# Matthew Koch, Carolyn Grum, Beth Pearson


from T040_M1_load_data import load_data as load_data
from T040_M1_load_data import add_average as add_avg


def student_list(dictionary: dict) -> list:
    """returns a dictionary as a list, 
    given a dictionary

    Preconditions:

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

student_list(school_dictionary_with_avg)
# student_list(health_dictionary_with_avg)
# student_list(age_dictionary_with_avg)
# student_list(failures_dictionary_with_avg)
