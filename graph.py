
from node import Node
from collections import deque



class Graph:
    def __init__(self):
        self.nodes = {} # a dictionary of sets

    def add_node(self, node):
        self.nodes[node] = set() # create an empty set for the node

    def add_edge(self, node1, node2):
        self.nodes[node1].add(node2) # add node2 to node1's neighbors set
        self.nodes[node2].add(node1) # add node1 to node2's neighbors set

    def get_neighbors(self, node):
        return self.nodes[node]
    
    def are_neighbors(self, node1, node2):
        # check if the robber moved one step in any direction
        robber_moved = abs(node1.robber[0] - node2.robber[0]) + abs(node1.robber[1] - node2.robber[1]) == 1
        robber_stayed = node1.robber == node2.robber
        # check if policemen stayed in the same place
        police1_stayed = node1.police1 == node2.police1
        police2_stayed = node1.police2 == node2.police2
        # check if policemen moved one step in any direction
        police1_moved = abs(node1.police1[0] - node2.police1[0]) + abs(node1.police1[1] - node2.police1[1]) == 1
        police2_moved = abs(node1.police2[0] - node2.police2[0]) + abs(node1.police2[1] - node2.police2[1]) == 1
        # check if police,en moved to the same place
        police_moved_to_same_place = node2.police1 == node2.police2
        # return True if either robber moved and policemen stayed or policemen moved and robber stayed
        return (robber_moved and police1_stayed and police2_stayed) or (police1_moved and police2_moved and robber_stayed and not police_moved_to_same_place)
    

    def create_graph(self, board_size):
        graph = self.__class__()
        # for i in range(board_size): # iterate over the rows of the robber
        #     for j in range(board_size): # iterate over the columns of the robber
        #         for k in range(board_size): # iterate over the rows of police1
        #             for l in range(board_size): # iterate over the columns of police1
        #                 for m in range(board_size): # iterate over the rows of police2
        #                     for n in range(board_size): # iterate over the columns of police2
        #                         robber = (i, j)
        #                         police1 = (k, l)
        #                         police2 = (m, n)
        #                         node = Node(robber, police1, police2)
        #                         graph.add_node(node)
        #                         print(f"Added node {node}")
        #                         for node1 in graph.nodes:
        #                             for node2 in graph.nodes:
        #                                 if node1 != node2 and self.are_neighbors(node1, node2):
        #                                     graph.add_edge(node1, node2)

        nodes = [Node((i, j), (k, l), (m, n)) for i in range(board_size)
                       for j in range(board_size) for k in range(board_size) for l in range(board_size)
                        for m in range(board_size) for n in range(board_size)]
        self.nodes = {node: set() for node in nodes}
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2 and self.are_neighbors(node1, node2):
                    # cops_in_same_place = node2.police1 == node2.police2
                    # if cops_in_same_place:
                    #     self.remove_node(node2)
                    # else:
                    self.add_edge(node1, node2)
        
        return graph
    
    def reverse_bfs(self, initial_node):
        ###### queue implementation #####
        queue = deque() # create a queue
        visited = set() # create a set of visited nodes
        parent = {} # create a dictionary of parents
        for node in self.nodes: # iterate over all nodes in the graph
            if self.is_goal(node): # if the node is a goal node
                queue.append(node)
                visited.add(node)
                parent[node] = None
        while queue:
            current_node = queue.popleft()
            if current_node == initial_node: # if the current node is the initial node
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = parent[current_node]
                    path.reverse()
                return path
            else:
                for neighbor in self.get_neighbors(current_node):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        parent[neighbor] = current_node
        return "No solution"
        ###### stack implementation ######
        # stack = []
        # visited = set()
        # parent = {}
        # for node in self.nodes:
        #     if self.is_goal(node):
        #         stack.append(node)
        #         visited.add(node)
        #         parent[node] = None
        # while stack:
        #     current_node = stack.pop()
        #     if current_node == initial_node:
        #         path = []
        #         while current_node:
        #             path.append(current_node)
        #             current_node = parent[current_node]
        #             path.reverse()
        #         return path
        #     else:
        #         for neighbor in self.get_neighbors(current_node):
        #             if neighbor not in visited:
        #                 stack.append(neighbor)
        #                 visited.add(neighbor)
        #                 parent[neighbor] = current_node
        # return "No solution"
        


    def is_goal(self, node):
        return node.robber == node.police1 or node.robber == node.police2

    def best_move(self, initial_node):
        ###### queue implementation #####
        queue = deque() # create a queue
        visited = set() # create a set of visited nodes
        parent = {} # create a dictionary of parents
        for node in self.nodes: # iterate over all nodes in the graph
            if self.is_goal(node): # if the node is a goal node
                queue.append(node)
                visited.add(node)
                parent[node] = None
        while queue:
            current_node = queue.popleft()
            if current_node == initial_node:
                first_move = parent[current_node]
                return first_move
            else:
                for neighbor in self.get_neighbors(current_node):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        parent[neighbor] = current_node
        return "No solution"
        ###### stack implementation ######
        # stack = []
        # visited = set()
        # parent = {}
        # for node in self.nodes:
        #     if self.is_goal(node):
        #         stack.append(node)
        #         visited.add(node)
        #         parent[node] = None
        # while stack:
        #     current_node = stack.pop()
        #     if current_node == initial_node:
        #         first_move = parent[current_node]
        #         return first_move
        #     else:
        #         for neighbor in self.get_neighbors(current_node):
        #             if neighbor not in visited:
        #                 stack.append(neighbor)
        #                 visited.add(neighbor)
        #                 parent[neighbor] = current_node
        # return "No solution"
    

    def print_grid(self, node, size):
        grid = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append("-")
            grid.append(row)
        for pos, symbol in [(node.robber, "R"), (node.police1, "P"), (node.police2, "P")]:
            grid[pos[0]][pos[1]] = symbol
        for row in grid:
            row_str = ' '.join(row)
            print(row_str)
