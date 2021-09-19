

"""BST 2"""

class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # print(self.data)
        if data == self.data:
            print(f'node {self.data} already exist ')
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

    def preorder_traversal(self):
        elements = [self.data]
        # visit left tree
        if self.left:
            elements += self.left.preorder_traversal()

        # visit right tree
        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def height(self):
        if self.data is not None:
            self.root = self.data
            return self._height(BinarySearchTreeNode(self.data), 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)


def build_tree(elements):
    root = BinarySearchTreeNode(elements[-1])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


# if __name__ == '__main__':
#     numbers = [0, -1, -5, 17, 4, 1, 20, 9, 23, 34, 18]
#
#     # tre = BinarySearchTreeNode(5)
#
#     tre = build_tree(numbers)
#     # for i in range(len(numbers)):
#     #     tre.add_child(numbers[i])
#
#
#
#     tre.add_child(1)
#     tre.add_child(4)
#     tre.add_child(2)
#     tre.add_child(61)
#     # tre.add_child(7)
#     # tre.add_child(82)
#     # tre.add_child(15)
#     # tre.add_child(10)
#     # tre.add_child(11)
#
#     # print(tre.search(12))
#
#     # print(tre.height())
#
#     # root = build_tree(numbers)
#     # print(root.calculate_sum())
#
#     # numbers = [17, 4, 1, 20, 9, 23, 18, 34]
#
#     # numbers = [15, 12, 7, 14, 27, 20, 23, 88]
#     # numbers_tree = build_tree(numbers)
#
#     # print("Input numbers:", numbers)
#     # print("Min:", numbers_tree.find_min())
#     # print("Max:", numbers_tree.find_max())
#     # print("Sum:", numbers_tree.calculate_sum())
#     # print("In order traversal:", numbers_tree.in_order_traversal())
#     # print("Pre order traversal:", numbers_tree.preorder_traversal())
#     # print("Post order traversal:", numbers_tree.postorder_traversal())
#
#     # countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
#     # country_tree = build_tree(countries)
#     # print(country_tree.find_min())
#
#     # print("UK is in the list? ", country_tree.search("UK"))
#     # print("Sweden is in the list? ", country_tree.search("Sweden"))








"""BST 1"""

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
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
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
        # print(cur_node, cur_height)
        return max(left_height, right_height)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        def num_children(n):
            num_children = 0
            if n.left_child is not None:
                num_children += 1
            if n.right_child is not None:
                num_children += 1
            return num_children

        # get the parent node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into different cases based on the
        # structure of tree @ node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:

            # remove reference to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # CASE 2 (node has a single child)
        if node_children == 1:
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            # replace the node to be deleted with its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

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

    def in_order_traversal(self):
        elements = []
        if self.root:
            self._in_order_traversal(elements, self.root)
        return elements

    def _in_order_traversal(self, elements, cur_node):
        if cur_node:
            self._in_order_traversal(elements, cur_node.left_child)
            elements.append(cur_node.value)
            self._in_order_traversal(elements, cur_node.right_child)

    def pre_order_traversal(self):
        elements = []
        if self.root:
            self._pre_order_traversal(elements, self.root)
        return elements

    def _pre_order_traversal(self, elements, cur_node):
        if cur_node:
            elements.append(cur_node.value)
            self._in_order_traversal(elements, cur_node.left_child)
            self._in_order_traversal(elements, cur_node.right_child)

    def post_order_traversal(self):
        elements = []
        if self.root:
            self._pre_order_traversal(elements, self.root)
        return elements

    def _post_order_traversal(self, elements, cur_node):
        if cur_node:
            self._in_order_traversal(elements, cur_node.left_child)
            self._in_order_traversal(elements, cur_node.right_child)
            elements.append(cur_node.value)

    def delete(self, value):
        if self.root:
            self._delete(self.root, value)
        else:
            print('Value not in tree.')

    def _delete(self, cur_node, value):

        if cur_node == value:
            cur_node.value = None
        elif cur_node.value < value:
            self._delete(cur_node.left_child, value)
        elif cur_node.value < value:
            self._delete(cur_node.right_child, value)


def fill_tree(tree, num_arr):
    for num in range(len(num_arr)):
        cur_elem = num_arr[num]
        tree.insert(cur_elem)
    return tree


numbers2 = [0, -1, -5, 17, 4, 1, 20, 9, 23, 34, 18]

tree = binary_search_tree()
fill_tree(tree, numbers2)


# print(tree.height())
# print(tree.print_tree())
tree.delete_value(0)
print(tree.in_order_traversal())

# print(node().__str__())

# tree = binary_search_tree()
#
# tree.insert(1)
# tree.insert(5)
# tree.insert(2)
# tree.insert(61)
# tree.insert(4)
# tree.insert(5)
# tree.insert(6)
# tree.insert(7)
# tree.insert(8)
# tree.insert(9)
# tree.insert(10)
