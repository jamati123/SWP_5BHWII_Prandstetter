
def paiiir(list, sum):
    x = [x for x in list for j in list if x + j == sum]
    coun = [i * 2 if i % 3 == 0 else i for i in range(0, len(list))]


def pairs(sum, list, count):
    len_list = len(list) - count
    listpair = []

    if list(count) + list(len_list) == sum:
        listpair.append(list[count] + list[len_list])
        pairs(sum, list, count + 1)
    elif count == 0:
        listpair.append('None')
    
    return listpair


def main():
    print(pairs(5, [1, 2, 3, 4, 5], 0))

if __name__ == "__main__":
    main()