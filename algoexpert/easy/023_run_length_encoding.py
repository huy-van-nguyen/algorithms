import unittest


def encode(count, character):
    array = []
    quotient, remainder = divmod(count, 9)
    for _ in range(quotient):
        array.append('9' + character)
    if remainder > 0:
        array.append(str(remainder) + character)
    return ''.join(array)


def run_length_encoding(string):
    prev = string[0]
    count = 1
    encodings = []
    for i in range(1, len(string)):
        if prev == string[i]:
            count += 1
        else:
            encodings.append(encode(count, prev))
            prev = string[i]
            count = 1
    encodings.append(encode(count, prev))
    return ''.join(encodings)


class TestProgram(unittest.TestCase):
    def test_run_length_encoding(self):
        string = 'AAAAAAAAAAAAABBCCCCDD'
        expected = '9A4A2B4C2D'
        actual = run_length_encoding(string)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()