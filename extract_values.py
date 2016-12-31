'''
Return a formatted string of names, from a list of dictionaries.

namelist([{'name': 'Brett'}, {'name': 'Bart'}, {'name': 'Betty'}])
namelist([{'name': 'Brett'}, {'name': 'Bart'}])
namelist([{'name': 'Brett'}])
namelist([])
'''


def namelist(names):

    names = [k['name'] for k in names]

    if len(names) == 0:
        return ''

    elif len(names) == 1:
        return names[0]

    print(', '.join(names[0:-1]) + ' & ' + names[-1])
    return ', '.join(names[0:-1]) + ' & ' + names[-1]

namelist([{'name': 'Brett'}, {'name': 'Bart'}, {'name': 'Betty'}])
