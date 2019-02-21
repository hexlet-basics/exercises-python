from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    does_contain = env.expect_defined('does_contain')
    assert_equal(does_contain('Renly', 'R'), True)
    assert_equal(does_contain('Renly', 'r'), False)
    assert_equal(does_contain('Tommy', 'm'), True)
    assert_equal(does_contain('Tommy', 'd'), False)
