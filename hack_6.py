"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = []
    icont = 0    
    
    if len(s) > 1:
        for i in s:  
            icont +=1
            if icont % 2 != 1: 
                result.append('-')
            else:
                result.append(str(icont))           
    else:
        result = ["0"]       
    return result   

r1_6 = fn_hack_6(["a","b","c","d","e"])
r2_6 = fn_hack_6([])

print(f"{r1_6} / {r2_6}")
