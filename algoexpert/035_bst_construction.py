import unittest


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self is None:
            return BinarySearchTree(value)
        if self.value <= value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        if self is None:
            return False
        else:
            if self.value == value:
                return True
            elif self.value > value:
                if self.left is None:
                    return False
                return self.left.contains(value)
            else:
                if self.right is None:
                    return False
                return self.right.contains(value)

    def minimum(self):
        if self.left is None:
            return self
        else:
            return self.left.minimum()

    def remove(self, value):
        if self is None:
            return self
        if self.value > value:
            if self.left is not None:
                self.left.remove(value)
        elif self.value < value:
            if self.right is not None:
                self.right.remove(value)
        else:
            if self.left is None:
                self = self.right
                return self
            elif self.right is None:
                self = self.left
                return self
            temp = self.right.minimum()
            self.value = temp.value
            self.right = self.right.remove(temp.value)
        return self


class TestProgram(unittest.TestCase):
    def test_binary_search_tree(self):
        root = BinarySearchTree(10)
        root.left = BinarySearchTree(5)
        root.left.left = BinarySearchTree(2)
        root.left.left.left = BinarySearchTree(1)
        root.left.right = BinarySearchTree(5)
        root.right = BinarySearchTree(15)
        root.right.left = BinarySearchTree(13)
        root.right.left.right = BinarySearchTree(14)
        root.right.right = BinarySearchTree(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))


if __name__ == '__main__':
    unittest.main()
