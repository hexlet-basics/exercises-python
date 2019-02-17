from hexlet.test import TestEnv, expect_output

with TestEnv() as env:
    fun = env.expect_defined('print_jaimes_line')

    with expect_output('JAIME: Farewell, my friend...'):
        fun('Farewell, my friend...')

    with expect_output('JAIME: attack!'):
        fun('attack!')
