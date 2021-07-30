

"""BST 2"""

class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            print(f'node {self.data} already exist ')
            return  # node already exist

        if data < self.data:
            # add data in left subtree
            if self.left:
                print(self.left.in_order_traversal())
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

        # print(self.data)

    def preorder_traversal(self):
        elements = [self.data]
        # elements.append(self.data)
        # visit left tree
        if self.left:
            elements += self.left.preorder_traversal()

        # visit right tree
        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def postorder_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.postorder_traversal()
        # visit right tree
        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    root = BinarySearchTreeNode(elements[-1])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [0, -1, -5, 17, 4, 1, 20, 9, 23, 18, 34]

    # tre = BinarySearchTreeNode(5)

    # tre.add_child(1)
    # tre.add_child(2)
    # tre.add_child(1)
    # tre.add_child(1)
    # tre.add_child(5)
    # tre.add_child(61)
    # tre.add_child(7)
    # tre.add_child(82)
    # tre.add_child(15)
    # tre.add_child(10)
    # tre.add_child(11)

    # print(tre.search(12))


    # root = build_tree(numbers)
    # print(root.calculate_sum())

    # numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    # numbers = [15, 12, 7, 14, 27, 20, 23, 88]
    # numbers_tree = build_tree(numbers)

    # print("Input numbers:", numbers)
    # print("Min:", numbers_tree.find_min())
    # print("Max:", numbers_tree.find_max())
    # print("Sum:", numbers_tree.calculate_sum())
    # print("In order traversal:", numbers_tree.in_order_traversal())
    # print("Pre order traversal:", numbers_tree.preorder_traversal())
    # print("Post order traversal:", numbers_tree.postorder_traversal())

    # countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    # country_tree = build_tree(countries)
    # print(country_tree.find_min())

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))








"""BST ???"""
class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # print(value)
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value already in tree!')

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)
        return False


def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for num in range(0, num_elems):
        cur_elem = randint(0, max_int)

        tree.insert(cur_elem)
    return tree


tree = binary_search_tree()

tree.insert(0)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(10)


# tree = fill_tree(tree)

tree.print_tree()


print('tree height: ' + str(tree.height()))
print(tree.search(10))
print(tree.search(2))
print(tree.search(9))
print(tree.search(90))


