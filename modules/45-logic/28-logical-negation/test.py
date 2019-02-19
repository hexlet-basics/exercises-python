from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    is_not_lannister_soldier = env.expect_defined('is_not_lannister_soldier')
    assert_equal(is_not_lannister_soldier(('blue', None)), True)
    assert_equal(is_not_lannister_soldier(('red', 'man')), True)
    assert_equal(is_not_lannister_soldier(('red', 'lion')), False)
    assert_equal(is_not_lannister_soldier(('blue', 'lion')), False)
    assert_equal(is_not_lannister_soldier(('red', None)), False)
