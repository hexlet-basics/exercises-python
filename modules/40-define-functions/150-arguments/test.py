from hexlet.test import TestEnv

with TestEnv() as env:
    fun = env.expect_defined('print_seq')
    with env.expect_output('0-0-0-0-0-'):
        fun('0-', 5)
