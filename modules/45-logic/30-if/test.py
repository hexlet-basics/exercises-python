from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    guess_number = env.expect_defined('guess_number')
    assert_equal(guess_number(100500), 'Try again!')
    assert_equal(guess_number(42), 'You win!')
