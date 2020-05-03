""" Global values."""

from cache import LRUCache
from typing import List
#from trajectory import Trajectory
#from handler import Handler

# The initial trajectories
TRAJECTORIES: List = []

# Common cache
CACHE = LRUCache(1000)

# Tail cache for megring from head
TAIL_CACHE = LRUCache(200)

HANDLERS: List = []

BLOCKED_HANDLERS: List = []
