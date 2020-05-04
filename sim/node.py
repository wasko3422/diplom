"""Node implementation."""
from __future__ import annotations

from typing import List
from values import TRAJECTORIES
from typing import Union

class Node:
    """Node."""
    
    def __init__(self, id: int, value: float, trajectory_id: int, params: list = []):
        self.id: int = id
        self.value: float = value
        self.params: list = params
        self.trajectory_id: int = trajectory_id
        self.index: int = 0 # index in trajectory's list
        

    def update_value(self, value):
        #TODO calculation of value
        self.value = value

    def get_next_node(self) -> Union[Node, None]:
        trajectory = TRAJECTORIES[self.trajectory_id]
        if len(trajectory) - 1 == self.index:
            return None
        return trajectory[self.index + 1]

    def get_trajectory(self):
        return TRAJECTORIES[self.trajectory_id]

    def exchange(self, node: Node):
        ####### TODO what to do with the same nodes
        curr_trajectory = self.get_trajectory()
        their_trajectory = node.get_trajectory()
        curr_trajectory.exchange(their_trajectory, self.index, node.index)

    def is_last(self) -> bool:
        return len(TRAJECTORIES[self.trajectory_id]) - 1 == self.index

    def __str__(self) -> str:
        return 'Node id: %s, value: %s, trajectory_id: %s' % (self.id, self.value, self.trajectory_id)

