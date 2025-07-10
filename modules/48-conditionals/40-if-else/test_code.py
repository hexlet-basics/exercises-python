import index


def test():
    assert index.normalize_url("yandex.ru") == "https://yandex.ru"
    assert index.normalize_url("http://yandex.ru") == "https://yandex.ru"
    assert index.normalize_url("https://yandex.ru") == "https://yandex.ru"
    assert index.normalize_url("httpsecurity.com") == "https://httpsecurity.com"
    assert (
        index.normalize_url("https://httpbin.org/redirect-to?url=http://google.com")
        == "https://httpbin.org/redirect-to?url=http://google.com"
    )
    assert (
        index.normalize_url("httpbin.org/redirect-to?url=https://google.com")
        == "https://httpbin.org/redirect-to?url=https://google.com"
    )
    assert (
        index.normalize_url("httpbin.org/redirect-to?url=http://google.com")
        == "https://httpbin.org/redirect-to?url=http://google.com"
    )
