import unittest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root, running_sum, sums):
    if root:
        running_sum += root.value
        if not root.left and not root.right:
            sums.append(running_sum)
            return
        preorder(root.left, running_sum, sums)
        preorder(root.right, running_sum, sums)


def branch_sums(root):
    sums = []
    preorder(root, 0, sums)
    return sums


class TestProgram(unittest.TestCase):
    def test_branch_sums(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)

        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)

        root.left.right.left = BinaryTree(10)

        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        expected = [15, 16, 18, 10, 11]
        actual = branch_sums(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
