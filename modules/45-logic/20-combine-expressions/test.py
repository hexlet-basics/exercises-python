from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    has_targarien_reference = env.expect_defined('has_targarien_reference')
    assert_equal(has_targarien_reference(''), False)
    assert_equal(has_targarien_reference('Targari'), False)
    assert_equal(has_targarien_reference('Targaryen'), False)
    assert_equal(has_targarien_reference('Targaryen'), True)
