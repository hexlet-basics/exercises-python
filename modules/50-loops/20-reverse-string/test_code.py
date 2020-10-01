from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    my_substr = env.expect_defined('my_substr')
    assert_equal(my_substr('got', 3), 'got')
    assert_equal(my_substr('got', 2), 'go')
    assert_equal(my_substr('got', 1), 'g')
