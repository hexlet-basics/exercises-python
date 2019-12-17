from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    is_arguments_for_substr_correct = env.expect_defined(
        'is_arguments_for_substr_correct')
    string = 'Sansa Stark';
    end = len(string) - 1
    assert_equal(is_arguments_for_substr_correct(string, -1, 0), False)
    assert_equal(is_arguments_for_substr_correct(string, 0, -1), False)
    assert_equal(is_arguments_for_substr_correct(string, end + 1, 0), False)
    assert_equal(is_arguments_for_substr_correct(string, end, 1), True)
    assert_equal(is_arguments_for_substr_correct(string, 3, 3), True)
