from hexlet.test import TestEnv, expect_output

with TestEnv() as env:
    fun = env.expect_defined('print_seq')
    with expect_output('0-0-0-0-0-'):
        fun('0-', 5)
