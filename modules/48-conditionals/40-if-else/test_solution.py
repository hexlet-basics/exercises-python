import solution


def test():
    assert solution.normalize_url("yandex.ru") == "https://yandex.ru"
    assert solution.normalize_url("http://yandex.ru") == "https://yandex.ru"
    assert solution.normalize_url("https://yandex.ru") == "https://yandex.ru"
    assert (
        solution.normalize_url("httpsecurity.com")
        == "https://httpsecurity.com"
    )
    assert (
        solution.normalize_url(
            "https://httpbin.org/redirect-to?url=http://google.com"
        )
        == "https://httpbin.org/redirect-to?url=http://google.com"
    )
    assert (
        solution.normalize_url(
            "httpbin.org/redirect-to?url=https://google.com"
        )
        == "https://httpbin.org/redirect-to?url=https://google.com"
    )
    assert (
        solution.normalize_url("httpbin.org/redirect-to?url=http://google.com")
        == "https://httpbin.org/redirect-to?url=http://google.com"
    )
