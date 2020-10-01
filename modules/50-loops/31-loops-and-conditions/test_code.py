from hexlet.test import TestEnv, assert_equal

STRING1 = 'A'
STRING2 = 'HELLO'
STRING3 = 'HELLO!'

SHOUT_STRING1 = 'A'
SHOUT_STRING2 = 'HELLO' * 10
SHOUT_STRING3 = 'HELLO!' * 100

with TestEnv() as env:
    shouter = env.expect_defined('shouter')
    assert_equal(shouter(STRING1), SHOUT_STRING1)
    assert_equal(shouter(STRING2), SHOUT_STRING2)
    assert_equal(shouter(STRING3), SHOUT_STRING3)
