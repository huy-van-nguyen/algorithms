import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_nodes_in_array(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def remove_duplicates_from_linked_list(linked_list):
    if linked_list is None:
        return None
    current = linked_list
    while current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return linked_list


class TestProgram(unittest.TestCase):
    def test_remove_duplicates_from_linked_list(self):
        test = LinkedList(1)
        test.next = LinkedList(1)
        test.next.next = LinkedList(3)
        test.next.next.next = LinkedList(4)
        test.next.next.next.next = LinkedList(4)
        test.next.next.next.next.next = LinkedList(4)
        test.next.next.next.next.next.next = LinkedList(5)
        test.next.next.next.next.next.next.next = LinkedList(6)
        test.next.next.next.next.next.next.next.next = LinkedList(6)
        expected = LinkedList(1)
        expected.next = LinkedList(3)
        expected.next.next = LinkedList(4)
        expected.next.next.next = LinkedList(5)
        expected.next.next.next.next = LinkedList(6)
        actual = remove_duplicates_from_linked_list(test)
        self.assertEqual(expected.get_nodes_in_array(), actual.get_nodes_in_array())


if __name__ == '__main__':
    unittest.main()
