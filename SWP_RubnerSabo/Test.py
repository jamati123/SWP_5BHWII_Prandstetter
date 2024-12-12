
a = [1,2,3,2,5]

for x in a:
    if a.count(x) == 2:
        print(2)
        break

y = "hi there"

try:
    print(y)
except NameError:
    print("not defined")
except:
    print("something else went wrong")

