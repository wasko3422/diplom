from typing import List
from node import Node
from trajectory import Trajectory


def generate_trajectories(nodes: int, nodes_per_trajectory: int) -> List[Trajectory]:

    node_id = 1
    trajectory_id = 1
    n: List[Node] = []
    
    # Create nodes
    for _ in range(nodes):

        # TODO make more complicated logic about values (!!!!!!!!)
        n.append(Node(node_id, 5, 1))
        node_id += 1
    

    # TODO more complicated logic with exchange and not merge

    out: List[Trajectory] = []
    for i in range(0, nodes, nodes_per_trajectory):
        t = Trajectory(trajectory_id)
        trajectory_id += 1

        # attach previous node for merge
        if len(out):
            t.add_node(out[-1][-1])
        for j in n[i:i+nodes_per_trajectory]:
            t.add_node(j)
        t.update_nodes_id()
        out.append(t)
    
    return out
