"""Handler implementaion"""
from __future__ import annotations

from trajectory import Trajectory, MovedTrajectory
from typing import List
from node import Node
from values import TRAJECTORIES, CACHE, TAIL_CACHE, HANDLERS
from cache import CacheStruct


class Handler:

    def __init__(self, first_node: Node, nodes_per_time: int):
        self.blocked: bool = False
        self.nodes_per_time: int = nodes_per_time
        self.read_only: bool = False  # update the cache
        self.node: Node = first_node
        self.value = 1 # TODO
        self.sleep: int = 0  # skip the loop

    def merge(self) -> bool:
        """
        ----[HEAD]> [TAIL]------>
        result of merge
        ------[HEAD/TAIL]----->
        """
        cache = TAIL_CACHE.get(self.node)
        if not cache:
            return False
        
        # Unblock
        self.blocked = False
        node = cache.value

        tail_trajectory = TRAJECTORIES[node.trajectory_id]
        head_trajectory = TRAJECTORIES[self.node.trajectory_id]

        if head_trajectory == tail_trajectory:
            raise('wtf')
        
        # Create new trajectory
        merged_trajectory = head_trajectory.copy()
        merged_trajectory.merge(tail_trajectory)

        # place merged trajectory at tail trajectory
        TRAJECTORIES[head_trajectory.trajectory_id] = merged_trajectory

        # Replace the tail trajectory with the old one
        trajectory_holder = MovedTrajectory(len(TRAJECTORIES)-1, len(head_trajectory)-1)
        TRAJECTORIES[node.trajectory_id] = trajectory_holder

        # Update current handler's values
        self.current_position = len(head_trajectory)
        self.trajectory_id = len(TRAJECTORIES-1)


        #remove from cash
        TAIL_CACHE._remove(cache)
        return True

    def exchange(self, struct: CacheStruct):
        """
        Current handler is the first

        input:
        <a.tail>------x------<a.head>
        <b.tail>---x--------<b.head>

        output:
        <a.tail>-----x-----<b.tail>
        <b.tail>---x-----<a.head>
        """

        second_handler = struct.handler

        if self == second_handler:
            # TODO
            self._self_exchange(struct)
            return

        # update the trajectories 
        self.node.exchange(struct.node)

        first_copy = Handler(struct.node, self.nodes_per_time)
        # make sure the new handler wont overtake the current hanlder
        first_copy.sleep = 2
        self.value /= 2
        first_copy.value = self.value

        # the second 
        second_copy = Handler(self.node, second_handler.nodes_per_time)
        second_copy.sleep = 2
        second_copy.value = second_handler.value / 2


        HANDLERS.extend([first_copy, second_copy])
        


    def _self_exchange(self, struct: CacheStruct):
        pass

    def handle(self) -> None:

        if self.blocked:
            return

        if self.sleep:
            self.sleep -= 1
            return

        if self.read_only:
            self._read_only()
            return

        # iterate over loop
        for _ in range(self.nodes_per_time):
            # If we have reached the end of a trajectory
            # Change the handler to blocked mode
            if self.node.is_last():
                self.blocked = True

                # Call merge method
                merged = self.merge()

                # if we merged continue the loop
                if merged:
                    continue
                return
            
            self.update_node(self.node)

            cache = CACHE.get_value(self.node.id)
            if cache:
                self.exchange(cache)
            else:
                # Add node to cache
                struct = CacheStruct(self.node, self)
                CACHE.set(self.node.id, struct)
            self.node = self.node.get_next_node()

    def update_node(self, node: Node) -> None:
        # TODO
        node.update_value()

    def _update_cache(self, trajectory: Trajectory) -> Node:
            node = trajectory[self.current_position]
            CACHE.set(node.id, self)
            self.current_position  += 1
            return node
    

    def _read_only(self) -> None:
        for _ in range(self.nodes_per_time):
            if self.node.is_last():
                return
            CACHE.set(self.node.id, self)
            self.node = self.node.get_next_node()

    def copy(self) -> Handler:
        copy = Handler(None, 0)
        copy.value = self.value
        copy.blocked = self.blocked
        return copy
    

if __name__ == "__main__":
    b = Handler(1, None)
    print(b)