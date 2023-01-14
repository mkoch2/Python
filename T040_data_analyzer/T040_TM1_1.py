# Matthew Koch, Carolyn Grum, Beth Pearson

from check_equal import check_equal as check


def test_load_data_keys(dictionary, sort_type_dictionary: str):
    r"""returns the number of tests passed and tests failed, 
    given a dictionary and a sort type dictionary

    Preconditions: None

    Examples:
    >>>tests_passed, tests_failed = test_keys(school_dictionary, 'School')
    Tests passed:  1
    Tests failed:  0
    >>>tests_passed, tests_failed = test_keys(health_dictionary, 'Health')
    Tests passed:  1
    Tests failed:  0
    >>>tests_passed, tests_failed = test_keys(age_dictionary, 'Age')
    Tests passed:  1
    Tests failed:  0
    """

    tests_passed = 0
    tests_failed = 0

    if sort_type_dictionary == 'School':

        # assert school_keys == {'GP', 'MB', 'CF', 'BD', 'MS'}
        passed = check({'GP', 'MB', 'CF', 'BD', 'MS'}, dictionary.keys())

        if passed:
            tests_passed += 1

        else:
            tests_failed += 1

    elif sort_type_dictionary == 'Age':

        # assert age_keys == {18, 17, 15, 16, 19, 22, 20, 21}
        passed = check({18, 17, 15, 16, 19, 22, 20, 21}, dictionary.keys())

        if passed:
            tests_passed += 1

        else:
            tests_failed += 1

    elif sort_type_dictionary == 'Health':

        # assert health_keys == {3, 5, 1, 2, 4}
        passed = check({3, 5, 1, 2, 4}, dictionary.keys())

        if passed:
            tests_passed += 1

        else:
            tests_failed += 1

    elif sort_type_dictionary == 'Failures':

        # assert failures_keys == {0, 3, 2, 1}
        passed = check({0, 3, 2, 1}, dictionary.keys())

        if passed:
            tests_passed += 1

        else:
            tests_failed += 1

    return tests_passed, tests_failed



