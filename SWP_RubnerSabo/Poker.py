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



anz = 5
pool = 52
for i in range(100):
    print(lottoziehung(anz,pool))

