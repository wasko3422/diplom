import matplotlib.pyplot as plt
import networkx as nx

def networkx_pagerank():
    tryout = nx.read_edgelist("src.edgelist")

    ans = nx.pagerank(tryout)
    #nx.draw(tryout)
    #plt.show()
    #print(type(ans), ans)

    unreadable = list(ans.items())

    res = []

    for i in range(len(unreadable)):
        res.append(list(unreadable[i]))

    for j in range(len(res)):
        res[j][0] = int(res[j][0])

    final = sorted(res, key=lambda item: item[0])

    print(final)
    input("vvedi dlya zakrytia chtoto\n")

if __name__ == "__main__":
    networkx_pagerank()