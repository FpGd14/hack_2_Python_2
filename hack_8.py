"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""



def fn_hack_8(s):
    result = s
    result1 = []
    icont = len(result) 
    letra = ""

    if icont  % 2 == 0:                    # par
        for i in reversed(result):
            letra = str(icont)
            result1.append(letra)
            icont -= 1 
    else:                                        # impar
         for i in reversed(result):
            letra = i + '-' + str(icont) 
            result1.append(letra)
            icont -= 1
    return result1


r1_8 = fn_hack_8(["a","b","c","d","e"])     # impar ["e-5","d-4","c-3","b-2","a-1"]
r2_8 = fn_hack_8(["a","b","c"])             # impar ["c-3","b-2","a-1"]
r3_8 = fn_hack_8(["a","b","c","d"])         # par   ["4","3","2","1"]
r4_8 = fn_hack_8(["a","b"])                 # par   ["2","1"]

print(f"{r1_8} / {r2_8} / {r3_8} / {r4_8}")