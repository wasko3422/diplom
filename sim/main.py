"""Main loop"""

import os

from values import TRAJECTORIES, HANDLERS
from handler import Handler
from typing import List
from generate import generate_trajectories

HANDLERS_COUNT: int = os.getenv("HANDLERS_COUNT", 10)


def main():
    
    # create trajectories
    TRAJECTORIES = generate_trajectories(100, 4)

    for i in range(len(HANDLERS_COUNT)):
        pass
        #HANDLERS.append(Handler(i, 2))
    
    ## main loop
    for i in range(100):
        for i in HANDLERS:
            i.handle()
        # filter out the hanlders you need to delete after handling a trajectory
        HANDLERS = list(filter(lambda x: not x.delete_after_trajectory), HANDLERS)

if __name__ == "__main__":
    main()
