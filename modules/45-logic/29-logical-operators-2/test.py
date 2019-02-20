from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    is_neutral_soldier = env.expect_defined('is_neutral_soldier')
    assert_equal(is_neutral_soldier('yellow', 'black'), True)
    assert_equal(is_neutral_soldier('red', 'yellow'), False)
    assert_equal(is_neutral_soldier('red', 'red'), False)
    assert_equal(is_neutral_soldier('black', 'black'), True)
