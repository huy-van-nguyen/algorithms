import unittest


def caesar_cipher_encryptor(string, key):
    # 97-122
    encryption = []
    for i in range(len(string)):
        j = ord(string[i]) + key % 26 if ord(string[i]) + key % 26 < 123 else ((ord(string[i]) + key % 26) % 123) + 97
        encryption.append(chr(j))
    return ''.join(encryption)


class TestProgram(unittest.TestCase):
    def test_caesar_cipher_encryptor(self):
        # string = 'xyz'
        # key = 2
        # expected = 'zab'
        string = 'abc'
        key = 52
        expected = 'abc'
        actual = caesar_cipher_encryptor(string, key)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()