""" Update and average implementation."""
from node import Node

def first_average(firs_node: Node, second_node: Node):
    mean = (firs_node.value + second_node.value) / 2
    firs_node.value, second_node.value = mean, mean

def first_update(node: Node):
    #todo 
    pass
