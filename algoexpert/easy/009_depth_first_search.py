import unittest


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array):
        array.append(self.name)
        for node in self.children:
            node.depth_first_search(array)
        return array


class TestProgram(unittest.TestCase):
    def test_depth_first_search(self):
        graph = Node("A")
        graph.add_child("B").add_child("C").add_child("D")
        graph.children[0].add_child("E").add_child("F")
        graph.children[2].add_child("G").add_child("H")
        graph.children[0].children[1].add_child("I").add_child("J")
        graph.children[2].children[0].add_child("K")
        expected = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
        actual = graph.depth_first_search([])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
