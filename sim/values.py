""" Global values."""

from cache import LRUCache
from typing import List

# The initial trajectories
TRAJECTORIES: List = []

# Common cache
CACHE = LRUCache(1000)

# Tail cache for megring from head
TAIL_CACHE = LRUCache(500)

HANDLERS: List = []

COUNT_EXCHANGED = 0
COUNT_MERGES = 0
COUNT_CREATED_HANDLERS =0
