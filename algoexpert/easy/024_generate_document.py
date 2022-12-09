import unittest


def generate_document(characters, document):
    dict = {}
    for character in characters:
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    for character in document:
        if character not in dict or dict[character] == 0:
            return False
        else:
            dict[character] -= 1
    return True


class TestProgram(unittest.TestCase):
    def test_generate_document(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"
        expected = True
        actual = generate_document(characters, document)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()