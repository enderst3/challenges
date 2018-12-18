"""
Being a bald man myself, I know the feeling of needing to keep it clean shaven. 
Nothing worse that a stray hair waving in the wind.

You will be given a string(x). Clean shaved head is shown as "-" and stray hairs are shown as "/". 
Your task is to check the head for stray hairs and get rid of them.

You should return the original string, but with any stray hairs removed. Keep count of them though, 
as there is a second element you need to return:

0 hairs --> "Clean!"
1 hair --> "Unicorn!"
2 hairs --> "Homer!"
3-5 hairs --> "Careless!"
>5 hairs --> "Hobo!"

So for this head: "------/------" you should return:

["-------------", "Unicorn!"]
"""

def bald(s):
    hairs = []
    type = ''
    for i in s:
        if i == '/':
            hairs.append(i)
    if len(hairs) > 5:
        type = 'Hobo!'
    if len(hairs) >= 3 and len(hairs) <= 5:
        type = 'Careless!'
    if len(hairs) == 2:
        type = 'Homer!'
    if len(hairs) == 1:
        type = 'Unicorn!'
    else:
        "Clean!"
    hair_cut = s.replace('/', '-')
    print(hair_cut, type)
    return [hair_cut, type]