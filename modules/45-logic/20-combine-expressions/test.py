from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    has_targaryen_reference = env.expect_defined('has_targaryen_reference')
    assert_equal(has_targaryen_reference(''), False)
    assert_equal(has_targaryen_reference('Targari'), False)
    assert_equal(has_targaryen_reference('targaryen'), False)
    assert_equal(has_targaryen_reference('Targaryen'), True)
