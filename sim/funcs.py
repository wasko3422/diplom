""" Update and average implementation."""
from node import Node
from nx_pagerank_test import networkx_pagerank

def first_average(firs_node: Node, second_node: Node):
    mean = (firs_node.value + second_node.value) / 2
    firs_node.value, second_node.value = mean, mean

def first_update(node: Node, value: float):
    node.value += value


def find_page_rank(trajectories):
    n = {}
    # sum up all the same nodes in all the same trajectories
    for nodes in trajectories:
        for node in nodes:
            if node.id in n:
                n[node.id] = [n[node.id][0] + node.value, n[node.id][1]+1]
            else:
                n[node.id] = [node.value, 1]
    
    sum = 0
    # find the mean and max
    for i in n.keys():
        n[i] = n[i][0] / n[i][1]
        sum += n[i]

    for i in n.keys():
        n[i] = n[i]/sum
    
    return n

def find_mean_error(t):

    errors = []
    nx = networkx_pagerank()

    for i in nx:
        errors.append([i[0], t[i[0]] / i[1]])

    return errors
    

    


