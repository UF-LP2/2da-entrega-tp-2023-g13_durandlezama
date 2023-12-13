from binarytree import Node as OriginalNode


class node(OriginalNode):
    """modificamos la clase nodo para que tenga valor"""

    def __init__(self, value, name, left=None, right=None):
        super().__init__(value, left, right)
        self.name = name
