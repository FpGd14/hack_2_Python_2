"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""  


def fn_hack_3(s):
    result = '' 
    result1 = '' 
    vowelc = ["@","3","¡","0","v"]
    _str = []   

    for Cambio1 in s.split():

        Cambio1 = s.maketrans("aeiou", "@3¡0v")
        result1 = s.translate(Cambio1)

        if result1[-1] in vowelc:
            content = result1[0].upper() + result1[1:-1] + result1[-1]
            _str.append(content)
        else:
            result += result1[0].upper() + result1[1:-1] + result1[-1].upper()
            _str.append(result)


    result = "".join(_str)       
    return result
  

r1_3 = fn_hack_3("fooziman")
r2_3 = fn_hack_3("barziman")
r3_3 = fn_hack_3("3q")
r4_3 = fn_hack_3("qu")
r5_3 = fn_hack_3("qux")


print(f"{r1_3} / {r2_3} / {r3_3} / {r4_3} / {r5_3} ")
