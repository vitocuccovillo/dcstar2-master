class Node:
    def __init__(self, state, parent_node=None):
        self.state = state
        self.parent = parent_node

    def path(self):
        if self.parent is None:
            return [self.state]
        else:
            return self.parent.path() + [self.state]

    # ridefinito ordinamento fra oggetti node, guardando lo stato!
    def __lt__(self, other):
        return self.state[1] < other.state[1]
