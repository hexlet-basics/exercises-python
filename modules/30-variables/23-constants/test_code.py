# FIXME

from hexlet.test import TestEnv

with TestEnv() as env:
    env.expect_defined('DRAGONS_BORN_COUNT')
    env.expect_equal('DRAGONS_BORN_COUNT', 3)
