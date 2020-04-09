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

    # set cache
    for i in range(len(TRAJECTORIES)):
        HANDLERS.append(Handler(i, 2))
    
    ## main loop
    for i in range(5000):
        for i in HANDLERS:
            i.handle()
            if i.blocked:
                ## TODO
                i.read_only = True
                pass
        


    



if __name__ == "__main__":
    main()
