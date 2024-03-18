"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
   
    result = s
    _ls = []

    for txt in s.split():
       if len(txt) % 2 != 0:
          _ls.append(txt)
       else:
          content = txt[1:-1] 
          _ls.append(content)

    result = "".join(_ls)
    return result

r1_4 = fn_hack_4("fooziman")
r2_4 = fn_hack_4("barziman")
r3_4 = fn_hack_4("qux")

print(f"{r1_4} / {r2_4} / {r3_4}")
