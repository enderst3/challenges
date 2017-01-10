'''
return the url with anything after the anchor (#) removed.
'''


def remove_hash(url):

    if '#' in url:
        print(url.rpartition('#')[0])
        return url.rpartition('#')[0]

    else:
        print(url)
        return url

remove_hash('www.whateversite.com#about')
remove_hash('www.whateversite.com?page=6')
