from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    flip_flop = env.expect_defined('flip_flop')
    assert_equal(flip_flop('flip'), 'flop')
    assert_equal(flip_flop('flop'), 'flip')
