def normalize_url(url):
    if 'http://' == url[:7]:
        domain = url[7:]
    else:
        domain = url
    return 'https://' + domain
