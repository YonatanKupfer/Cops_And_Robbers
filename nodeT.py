class Node:
    def __init__(self, robber, police1, police2):
        self.robber = robber # a tuple of (i, j) coordinates
        self.police1 = police1 # a tuple of (k, l) coordinates
        self.police2 = police2 # a tuple of (m, n) coordinates

    def __eq__(self, other):
        return self.robber == other.robber and self.police1 == other.police1 and self.police2 == other.police2
    
    def __hash__(self):
        return hash((self.robber, self.police1, self.police2))
    
    def __repr__(self):
        return f"Node({self.robber}, {self.police1}, {self.police2})"
    
    def __str__(self):
        return f"Node({self.robber}, {self.police1}, {self.police2})"
        