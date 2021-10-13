from Node import Node


class BinaryTree:

    def __init__(self, arr):
        self.root = Node(0)
        available_nodes = [self.root]
        for index in range(len(arr)):
            if index % 2 == 0:
                node = Node(arr[index])
                node.parent = available_nodes[-1]
                available_nodes[-1].left = node
                available_nodes.insert(0, node)
            else:
                node = Node(arr[index])
                node.parent = available_nodes[-1]
                available_nodes[-1].right = node
                available_nodes.insert(0, node)
                available_nodes.pop(-1)
