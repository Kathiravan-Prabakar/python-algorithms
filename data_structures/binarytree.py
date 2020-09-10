from typing import Optional

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None

def inorder(tree: Node) -> None:
    if tree:
        inorder(node.left)
        print(node.val)
        inorder(node.right)


node = Node(1)
node.left = Node(2)
node.right = Node(3)
inorder(node)