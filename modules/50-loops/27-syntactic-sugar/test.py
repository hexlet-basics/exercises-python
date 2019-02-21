from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    count_chars = env.expect_defined('count_chars')
    string = 'If I look back I am lost'
    assert_equal(count_chars(string, 'I'), 3)
    assert_equal(count_chars(string, 'z'), 0)
    assert_equal(count_chars(string, 'o'), 3)
