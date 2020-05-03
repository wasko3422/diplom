def read_from_src_edgelist_to_idvalue():
    encounters = dict()

    src = open("src.edgelist", "r")

    textik = src.readlines()

    for i in range(len(textik)):

        a = textik[i].rstrip("\n").split()
        textik[i] = a
        #print(textik[i])

        key1 = int(textik[i][0])
        key2 = int(textik[i][1])
        encounters[key1] = encounters.get(key1, 0)+1
        encounters[key2] = encounters.get(key2, 0)+1

    src.close()
    #print(encounters)

    pre = sorted(encounters.items(), key=lambda item: item[0])
    #print(type(pre), pre)
    res = []
    for i in range(len(pre)):
        res.append(list(pre[i]))

    print("id,value list, value = number of connections")
    print(res)
    return res

read_from_src_edgelist_to_idvalue()
input("vvedi dlya zakrytia chtoto\n")