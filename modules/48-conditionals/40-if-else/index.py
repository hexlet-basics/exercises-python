def normalize_url(url):
    prefix = "https://"
    if url[:8] == prefix:
        return url
    else:
        if url[:7] == "http://":
            return prefix + url[7:]
        else:
            return prefix + url
