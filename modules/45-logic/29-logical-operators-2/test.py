from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    in_neutral_soldier = env.expect_defined('in_neutral_soldier')
    assert_equal(in_neutral_soldier('yellow', 'black'), True)
    assert_equal(in_neutral_soldier('red', 'yellow'), False)
    assert_equal(in_neutral_soldier('red', 'red'), False)
    assert_equal(in_neutral_soldier('black', 'black'), True)
