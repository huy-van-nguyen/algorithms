import unittest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root, level):
    if root:
        level += 1
        global sum
        sum += level
        preorder(root.left, level)
        preorder(root.right, level)


def level_order(root):
    if not root:
        return None
    queue = []
    queue.append(root)
    sum = 0
    level = -1
    while len(queue) > 0:
        count = len(queue)
        level += 1
        while count > 0:
            sum += level
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            count -= 1
    return sum


def node_depths(root):
    global sum
    sum = 0
    preorder(root, -1)
    return sum


class TestProgram(unittest.TestCase):
    def test_node_depths(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)

        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)

        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        expected = 16
        actual = node_depths(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
