from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    is_lannister_soldier = env.expect_defined('is_lannister_soldier')
    assert_equal(is_lannister_soldier('blue', None), False)
    assert_equal(is_lannister_soldier('red', 'man'), False)
    assert_equal(is_lannister_soldier('red', 'lion'), True)
    assert_equal(is_lannister_soldier('blue', 'lion'), True)
    assert_equal(is_lannister_soldier('red', None), True)
