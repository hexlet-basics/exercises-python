from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    mysubstr = env.expect_defined('mysubstr')
    assert_equal(mysubstr('got', 3), 'got')
    assert_equal(mysubstr('got', 2), 'go')
    assert_equal(mysubstr('got', 1), 'g')
