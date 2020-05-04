"""Trajectory implemention."""
from __future__ import annotations

from node import Node
from typing import List

class Trajectory:

    def __init__(self, id: int, nodes: List[Node]=[]):
        self.id: int = id
        self.is_handled: bool = False
        self.nodes: List[Node] = nodes

    def add_node(self, node: Node):
        self.nodes.append(node)
        ##node.update_value(5)

    def __str__(self):
        return '%s' % self.nodes

    def __len__(self) -> int:
        return len(self.nodes)

    def __getitem__(self, s: slice) -> Node:
        return self.nodes.__getitem__(s)

    def pop(self, index:int) -> Node:
        return self.nodes.pop(index)

    def merge(self, trajectory: Trajectory):
        # TODO update head/tail node(?)
        self.nodes.extend(trajectory.nodes[1:])
        self.update_nodes_id()

    def exchange(self, trajectory: Trajectory, current_index: int, their_index: int):

        ## TODO all
        curr_nodes = self.nodes[:current_index+1].extend(trajectory[their_index+1:])
        their_nodes = trajectory.nodes[:their_index+1].extend(self.nodes[current_index+1:])

        self.nodes = curr_nodes
        trajectory.nodes = their_nodes

        self.update_nodes_id()
        trajectory.update_nodes_id()


    def copy(self) -> Trajectory:
        return Trajectory(self.nodes)

    def update_nodes_id(self):
        """ Update trajectory_id and index in nodes"""
        for i, k in enumerate(self.nodes):
            k.trajectory_id = self.id
            k.index = i

    def get_first_node(self) -> Node:
        return self.nodes[0]


class MovedTrajectory:

    def __init__(self, moved_to: int, shifted: int):
        self.moved_to: int = moved_to
        self.shifted: int = shifted
