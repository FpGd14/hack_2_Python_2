"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    icont = 0
    vowels = 0
    vowels1 = "a", "e", "i", "o", "u"
    result1 = ""
    _ls = []

    for i in result:
        if icont == 2:  
            if vowels == 1: 
                result1 = result1 + "-"
                result1 = result1 + i
                vowels = 0
                icont = 0
            else:
                if i in vowels1:
                    vowels = 1
                result1 = result1 + "-"
            if icont != 0:
                icont = -1
        else:
            result1 = result1 + i
        icont += 1     
    
    _ls.append(result1)   

    result = "".join(_ls)
    return result

r1_5 = fn_hack_5("fooziman")
r2_5 = fn_hack_5("barziman")
r3_5 = fn_hack_5("qux")
r4_5 = fn_hack_5("eq")

print(f"{r1_5} / {r2_5} / {r3_5} / {r4_5}")