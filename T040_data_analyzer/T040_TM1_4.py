# Matthew Koch, Carolyn Grum, Beth Pearson

from check_equal import check_equal as check


def calc_avg_grade(student_info: dict):
    grade_1 = student_info.get('G1')
    grade_2 = student_info.get('G2')
    grade_3 = student_info.get('G3')

    avg_grade = (grade_1 + grade_2 + grade_3) / 3
    avg_grade = format(avg_grade, '.2f')

    return avg_grade

# ------------------


def test_add_average(dictionary: dict, dictionary_with_avg: dict):
    r"""prints the total number of tests failed and tests passed for all dictionaries, given the sort type dictionary

    preconditions: None

    Examples:
    >>>tests_passed, tests_failed = test_avg(
    school_dictionary, school_dictionary_with_avg)
    Tests passed:  1
    Tests failed:  0

    """

    tests_passed = 0
    tests_failed = 0

    keys = dictionary.keys()
    keys_with_avg = dictionary.keys()

    # (1) The number of students in the dictionary does not change.
    total_num_students = 0
    for key in keys:
        key_list = dictionary.get(key)
        total_num_students += len(key_list)

    total_num_students_with_avg = 0
    for key in keys_with_avg:

        key_list = dictionary_with_avg.get(key)
        total_num_students_with_avg += len(key_list)

        # (2) The G_Avg key is added to the student dictionary.

        for student_info in key_list:
            avg = student_info.get('G_Avg')

            # assert avg != None

            is_avg = (avg != None)

            passed = check(True, is_avg)

            if passed:
                tests_passed += 1

            else:
                tests_failed += 1

            avg_grade = calc_avg_grade(student_info)
            # assert avg_grade == avg
            passed = check(avg, avg_grade)

            if passed:
                tests_passed += 1

            else:
                tests_failed += 1

    # assert total_num_students == total_num_students_with_avg
    passed = check(total_num_students_with_avg, total_num_students)

    if passed:
        tests_passed += 1

    else:
        tests_failed += 1

    return tests_passed, tests_failed








