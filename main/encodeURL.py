# def shorten_url(url, id):
#     short_url = ecncode

def encode(id):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base = len(characters)
    short_url = ''
    while id > 0:
        val = id % base
        short_url += characters[val]
        id = id // base
    return short_url
