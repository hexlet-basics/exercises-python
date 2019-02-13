from hexlet.test import *

with Module() as module:
    module.expect_defined('DRAGONS_BORN_COUNT')
    module.expect_eq('DRAGONS_BORN_COUNT', 3)
