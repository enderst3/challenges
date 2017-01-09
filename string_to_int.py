'''
write a myParseInt method with the following rules:
- It should make the conversion if the given string only contains a single
integer value (and eventually spaces including tabs, line feeds.at both ends)
- For all other strings (including the ones representing float values),
it should return NaN
'''


def my_parse_int(string):

    try:
        print(int(string))
        return int(string)

    except ValueError:
        print("NaN")
        return "NaN"

my_parse_int("1")
my_parse_int("  1 ")
my_parse_int("08")
my_parse_int("5 friends")
my_parse_int("16.5")
