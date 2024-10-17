import random

def lottoziehung(ziehungen = 6,pool = 45):
    zahlen = []
    for x in range(ziehungen):
        ziehung = random.randint(1,pool)
        if ziehung not in zahlen:
            zahlen.append(ziehung)
        else:
            x =-1
    return zahlen

wie_viele = 6
bis = 45


dicto = {}
for _ in range(1000):
    werte = lottoziehung(wie_viele,bis) 
    for i in werte:
        if i not in dicto:
            dicto[i] = 1
        elif i in dicto:
            dicto[i] = dicto[i] + 1


#for s in dicto:
#    print(s, "|", str(dicto[s]))            

dictosort = dict(sorted(dicto.items()))
for s in dictosort:
    print(s, "|", str(dictosort[s]))








