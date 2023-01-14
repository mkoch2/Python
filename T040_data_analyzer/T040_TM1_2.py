# Matthew Koch, Carolyn Grum, Beth Pearson


from check_equal import check_equal as check


def test_dictionary_values_size_of_lists(dictionary, sort_type_dictionary: str):
    r"""prints the total number of tests failed and tests passed for all dictionaries, given the sort type dictionary

    preconditions: None

    Examples:
    >>>tests_passed, tests_failed = test_lists_size(school_dictionary, 'School')
    Tests passed:  1
    Tests failed:  0
    >>>tests_passed, tests_failed = test_lists_size(school_dictionary, 'Health')
    Tests passed:  1
    Tests failed:  0
    >>>tests_passed, tests_failed = test_lists_size(school_dictionary, 'Age')
    Tests passed:  1
    Tests failed:  0
    """

    tests_passed = 0
    tests_failed = 0

    if sort_type_dictionary == 'School':
        school_dictionary = dictionary
        school_keys = school_dictionary.keys()

        school_expected_sizes = {
            'GP': 79, 'MB': 80, 'CF': 80, 'BD': 80, 'MS': 76}

        for key in school_keys:
            school_list = school_dictionary.get(key)
            school_list_size = len(school_list)

            # assert len(school_list) == school_expected_sizes.get(key)
            passed = check(len(school_list), school_expected_sizes.get(
                key))

            if passed:
                tests_passed += 1

            else:
                tests_failed += 1

    if sort_type_dictionary == 'Health':
        health_dictionary = dictionary
        health_keys = health_dictionary.keys()

        health_expected_sizes = {3: 91, 5: 146, 1: 47, 2: 45, 4: 66}

        for key in health_keys:
            health_list = health_dictionary.get(key)
            health_list_size = len(health_list)

            # assert len(health_list) == health_expected_sizes.get(key)
            passed = check(len(health_list), health_expected_sizes.get(
                key))

            if passed:
                tests_passed += 1

            else:
                tests_failed += 1

    if sort_type_dictionary == 'Age':
        age_dictionary = dictionary
        age_keys = age_dictionary.keys()

        age_expected_sizes = {18: 82, 17: 98, 15: 82,
                              16: 104, 19: 24, 22: 1, 20: 3, 21: 1}

        for key in age_keys:
            age_list = age_dictionary.get(key)
            age_list_size = len(age_list)

            # assert len(age_list) == age_expected_sizes.get(key)
            passed = check(len(age_list), age_expected_sizes.get(
                key))

            if passed:
                tests_passed += 1

            else:
                tests_failed += 1

    if sort_type_dictionary == 'Failures':
        failures_dictionary = dictionary
        failures_keys = failures_dictionary.keys()

        failures_expected_sizes = {0: 312, 3: 16, 2: 17, 1: 50}

        for key in failures_keys:
            failures_list = failures_dictionary.get(key)
            failures_list_size = len(failures_list)

            # assert len(failures_list) == failures_expected_sizes.get(key)
            passed = check(len(failures_list), failures_expected_sizes.get(
                key))

            if passed:
                tests_passed += 1

            else:
                tests_failed += 1

    return tests_passed, tests_failed



