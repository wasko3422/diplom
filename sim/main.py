"""Main loop"""

import os

from values import TRAJECTORIES, HANDLERS
from handler import Handler
from typing import List
from data import load_trajectories
from funcs import first_average, first_update


HANDLERS_COUNT: int = os.getenv("HANDLERS_COUNT", 10)
PICKLED_TRAJECTORIES_FILE: str = os.getenv("PICKLED_TRAJECTORIEs_FILE", "data_1.pickle")
NODES_PER_TIME: int = os.getenv("NODES_PER_TIME", 3)


def main():
    
    # create trajectories
    global TRAJECTORIES, HANDLERS
    TRAJECTORIES = load_trajectories(PICKLED_TRAJECTORIES_FILE)

    for i in range(HANDLERS_COUNT):
        HANDLERS.append(
            Handler(
                first_node= TRAJECTORIES[i].get_first_node(), 
                nodes_per_time=NODES_PER_TIME, 
                update=first_update,
                average=first_average,
                ),
            )
    
    ## main loop
    for _ in range(100):
        i = 0
        while i < len(HANDLERS):
            h: Handler = HANDLERS[i]
            h.handle()

        # filter out the hanlders you need to delete after handling a trajectory
        HANDLERS = list(filter(lambda x: not x.delete_after_trajectory), HANDLERS)

if __name__ == "__main__":
    main()
