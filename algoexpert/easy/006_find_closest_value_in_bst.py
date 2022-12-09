import unittest


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_closest_value_in_bst_with(tree, target, current_closest):
    if tree is None or current_closest == target:
        return current_closest
    value = tree.value
    if current_closest is None:
        current_closest = value
    if abs(target - value) <= abs(target - current_closest):
        current_closest = value
    if target > value:
        return find_closest_value_in_bst_with(tree.right, target, current_closest)
    else:
        return find_closest_value_in_bst_with(tree.left, target, current_closest)


def find_closest_value_in_bst(tree, target):
    return find_closest_value_in_bst_with(tree, target, None)


def find_closest_value_in_bst_none_recursion(tree, target):
    if tree is None:
        return None
    closest = tree.value
    while tree is not None:
        if abs(target - tree.value) < abs(target - closest):
            closest = tree.value
        if target > tree.value:
            tree = tree.right
        elif target < tree.value:
            tree = tree.left
        else:
            return tree.value
    return closest


class TestProgram(unittest.TestCase):
    def test_find_closest_value_in_bst(self):
        root = BinarySearchTree(10)
        root.left = BinarySearchTree(5)
        root.right = BinarySearchTree(15)

        root.left.left = BinarySearchTree(2)
        root.left.right = BinarySearchTree(5)

        root.left.left.left = BinarySearchTree(1)

        root.right.left = BinarySearchTree(13)
        root.right.right = BinarySearchTree(22)

        root.right.left.right = BinarySearchTree(14)

        expected = 13
        actual = find_closest_value_in_bst(root, 12)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
