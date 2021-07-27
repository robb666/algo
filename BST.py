
"""BST 2"""
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            print(self.left)
            elements = elements + [self.left.in_order_traversal()]

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += [self.right.in_order_traversal()]


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [0, 17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())








"""BST ???"""
# class node:
#     def __init__(self, value=None):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#
# class binary_search_tree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         # print(value)
#         if self.root is None:
#             self.root = node(value)
#             # print(self.root.value)
#         else:
#             self._insert(value, self.root)
#
#     def _insert(self, value, cur_node):
#         if cur_node is None:
#             return
#         if value < cur_node.value:
#             if cur_node.left_child is None:
#                 cur_node.left_child = node(value)
#             else:
#                 self._insert(value, cur_node.left_child)
#         elif value > cur_node.value:
#             if cur_node.left_child is None:
#                 cur_node.right_child = node(value)
#             else:
#                 self._insert(value, cur_node.right_child)
#         else:
#             print('Value already in tree!')
#
#     def print_tree(self):
#         if self.root is not None:
#             self._print_tree(self.root)
#
#     def _print_tree(self, cur_node):
#         if cur_node is not None:
#             self._print_tree(cur_node.left_child)
#             print(cur_node.value)
#             self._print_tree(cur_node.right_child)
#
#
# def fill_tree(tree, num_elems=20, max_int=1000):
#     from random import randint
#     for num in [2, 0, 1, 5, 9, 11, 12]:
#         # cur_elem = randint(0, max_int)
#         tree.insert(num)
#     return tree
#
#
# tree = binary_search_tree()
# tree = fill_tree(tree)
#
# tree.print_tree()
