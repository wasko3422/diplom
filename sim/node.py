"""Node implementation."""

from typing import List

class Node:
    """Node."""
    def __init__(self, id: int, value: float, node: List[Node] = [], params: list = []):
        self.id = id
        self.value = value
        # for graph???
        self.nodes = nodes
        self.params = params
        

    def update_value(self, value):
        #TODO calculation of value
        self.value = value

    def add_node(self, node: Node):
        self.nodes.append(node)
