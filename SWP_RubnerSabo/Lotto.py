import random

def lottoziehung(ziehungen,pool):
    zahlen = []
    check = False
    for x in range(1,ziehungen):
        check = False
        ziehung = random.randint(1,pool)
        if ziehung not in zahlen:
            zahlen.append(ziehung)
        else:
            x =-1
    return zahlen


dicto = {}
for z in range(1,1000):
    werte = lottoziehung(6,45) 
    for i in werte:
        if i not in dicto:
            dicto[i] = 1
        elif i in dicto:
            dicto[i] = dicto[i] + 1

dictosort = dict(sorted(dicto.items()))
for s in dictosort:
    print(s, "|", str(dictosort[s]))







