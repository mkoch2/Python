# Matthew Koch, Carolyn Grum, Beth Pearson

from check_equal import check_equal as check


def test_load_data_student_entries(dictionary: dict, sort_type_dictionary: str):
    r"""prints the total number of tests failed and tests passed for all dictionaries, given the sort type dictionary

    preconditions: None

    Examples:
    >>>tests_passed, tests_failed = test_entries(
    school_dictionary, 'School')
    Tests passed:  1
    Tests failed:  0
    >>>tests_passed, tests_failed = test_entries(
    school_dictionary, 'Health')
    Tests passed:  1
    Tests failed:  0
    >>>tests_passed, tests_failed = test_entries(
    school_dictionary, 'Age')
    Tests passed:  1
    Tests failed:  0
    """

    tests_passed = 0
    tests_failed = 0

    student = {'School': 'MS', 'Age': 18, 'StudyTime': 1, 'Failures': 0,
               'Health': 5, 'Absences': 0, 'G1': 11, 'G2': 12, 'G3': 10}

    keys = dictionary.keys()

    found_student = False

    # iterate through dicitonary keys
    for key in keys:
        key_list = dictionary.get(key)
        # Iterate through key list
        for student_info in key_list:

            student_info.update({sort_type_dictionary: key})

            if student_info == student:

                found_student = True

    # Check if student is found
    passed = check(True, found_student)

    if passed:
        tests_passed += 1

    else:
        tests_failed += 1

    return tests_passed, tests_failed



