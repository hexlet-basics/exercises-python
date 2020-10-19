def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    else:
        if url[:7] == 'http://':
            return https + url[7:]
        else:
            return https + url
