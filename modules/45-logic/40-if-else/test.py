from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    normalize_url = env.expect_defined('normalize_url')
    assert_equal(normalize_url('yandex.ru'), 'https://yandex.ru')
    assert_equal(normalize_url('http://yandex.ru'), 'https://yandex.ru')
    assert_equal(normalize_url('https://yandex.ru'), 'https://yandex.ru')
