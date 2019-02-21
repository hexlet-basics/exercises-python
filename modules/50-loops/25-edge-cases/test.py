from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    is_arguments_for_substr_correct = env.expect_defined(
        'is_arguments_for_substr_correct')
    string = 'Sansa Stark';
    result1 = is_arguments_for_substr_correct(string, -1, 3)
    assert_equal(result1, False)
    result2 = is_arguments_for_substr_correct(string, 4, 100)
    assert_equal(result2, False)
    result3 = is_arguments_for_substr_correct(string, 10, 10)
    assert_equal(result3, False)
    result4 = is_arguments_for_substr_correct(string, 11, 1)
    assert_equal(result4, False)
    result5 = is_arguments_for_substr_correct(string, 3, 3)
    assert_equal(result5, True)
