from random import choice as rchoice


def read_from_src_edgelist_to_idvalue():
    encounters = dict()
    contacts = [[] for i in range(380)]
    src = open("src.edgelist", "r")

    textik = src.readlines()

    for i in range(len(textik)):
        a = textik[i].rstrip("\n").split()
        textik[i] = a
        # print(textik[i])

        key1 = int(textik[i][0])
        key2 = int(textik[i][1])
        encounters[key1] = encounters.get(key1, 0) + 1
        encounters[key2] = encounters.get(key2, 0) + 1
        contacts[key1].append(key2)
        contacts[key2].append(key1)

    src.close()
    # print(encounters)

    pre = sorted(encounters.items(), key=lambda item: item[0])
    # print(type(pre), pre)
    res = []
    del contacts[0]
    for i in range(len(pre)):
        curr = list(pre[i]) + [contacts[i]]
        # print(curr)
        res.append(curr)

    # print("id, value, list of conns")
    # print(res)
    # print(contacts)
    return res


def traverse(offset_start, source_graph):
    current_trajectory = set()
    next_index = offset_start - 1
    #print(f"next_number = {next_index + 1}")
    options = source_graph[next_index][2]
    #print(f"options = {options}")
    while not set(options).issubset(current_trajectory):
        current_trajectory.add(next_index + 1)
        next_index = rchoice(options) - 1
        #print(f"next_number = {next_index + 1}")
        options = source_graph[next_index][2]
        #print(f"options = {options}")
    # print(f"current_trajectory = {current_trajectory}")
    # print(f"curent node = {offset_start}")

    # print(f"current_trajectory = {current_trajectory}")
    if len(current_trajectory) < 3:
        current_trajectory = traverse(next_index, source_graph)
    return current_trajectory


def main():
    test = read_from_src_edgelist_to_idvalue()
    unprocessed = set([i + 1 for i in range(len(test))])
    final = []

    while len(unprocessed) > 0:
        current = traverse(rchoice(list(unprocessed)), test)
        unprocessed.difference_update(current)
        # print(unprocessed)
        final.append(list(current))

    print("final =", final)
    return final


main()
