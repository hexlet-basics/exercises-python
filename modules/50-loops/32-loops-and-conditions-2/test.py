from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    get_even_numbers_up_to = env.expect_defined('get_even_numbers_up_to')
    assert_equal(get_even_numbers_up_to(9), "2,4,6,8,")
    assert_equal(get_even_numbers_up_to(15), "2,4,6,8,10,12,14,")
    assert_equal(get_even_numbers_up_to(2), "2,")
