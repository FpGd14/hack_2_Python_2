"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    abcedario = [' ', 'a', 'b', 'c','d', 'e', 'f','g', 'h', 'i','j', 'k', 'l','m', 'n', 'o','p', 'q', 'r','s', 't', 'u','v', 'w', 'x','y', 'z']
    contador = 0
    num1 = 0
    diccio2 = {}
    i = 0
    result1 = []
    
    for x in result: 
        if i % 2 == 0: 
            for num in x: #tomo el elemento como diccionario
                icont = 0  
                for letra in abcedario:
                    if letra == num:
                        contador = icont

                    elif letra == x[num]:
                        num1 = icont

                    icont += 1
                #se crea aqui el elemento del diccionario
                
                elemento = {
                    str(contador) : str(num1)
                }
                result1.append(elemento)
               
        else:
            indicador = 0
            var1 = 0
            var2 = 0
            for num in x:
                icont = 0 
                for letra in abcedario:
                    if letra == num:
                        if indicador == 0:
                            var2 = str(icont)
                            indicador = 1
                        else:
                            var1 = str(icont)

                        
                    icont += 1
                
            diccio2= { var1, var2}
            result1.append(diccio2)

        i += 1
    return result1

print(fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}]))