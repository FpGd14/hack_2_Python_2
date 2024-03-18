"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    textsalid = {}
    letras = 'foo'
    letra = 'k'


    for i in result:
        if i == letras:
           d = result[i]
           i = i.capitalize()
           d = d.capitalize()
           r = ''
           for b in d:
               if b != letra:
                   r = r + b
           textsalid = {
                i : r
            }       
    return textsalid

r1_9 = fn_hack_9({"foo":"fookziman","bar":"barziman"})  

print(f"{r1_9}")
