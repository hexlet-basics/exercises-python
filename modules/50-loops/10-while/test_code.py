from hexlet.test import TestEnv

with TestEnv() as env:
    print_numbers = env.expect_defined('print_numbers')
    with env.expect_output('2\n1\nfinished!'):
        print_numbers(2)
    with env.expect_output('4\n3\n2\n1\nfinished!'):
        print_numbers(4)
