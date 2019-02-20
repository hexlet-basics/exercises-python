from hexlet.test import TestEnv

with TestEnv() as env:
    fun = env.expect_defined('print_jaimes_line')

    with env.expect_output('JAIME: Farewell, my friend...'):
        fun('Farewell, my friend...')

    with env.expect_output('JAIME: attack!'):
        fun('attack!')
