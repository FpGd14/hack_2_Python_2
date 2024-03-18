"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = []
    icont = 1
    
    if len(s) > 1:
        while icont <= len(s):
            if icont % 2 == 0: 
                result.append(icont)
            else:
                result.append(str(icont))  
            icont += 1      
    else:
        result = [0]
    return result

r1_7 = fn_hack_7(["a","b","c","d","e"])
r2_7 = fn_hack_7([])

print(f"{r1_7} / {r2_7}")

