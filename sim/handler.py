"""Handler implementaion"""


class Handler:

    def __init__(self, id: int, global_trajectory_id: int, nodes_per_time: int, cache):
        self.id = id
        self.global_trajectory_id = global_trajectory_id
        self.global_current_node = 0
        self.blocked = False
        self.nodes_per_time = nodes_per_time
        self.nodes = []
        self.cache = cache
    
    def update_nodes(self, value):
        for node in self.nodes:
            #TODO normal update_value
            node.update_value(value)

    def merge_trajectories(self, handler: Handler):
        #TODO

    def exchange_nodes(self, hanlder: Handler, node: Node):
        
