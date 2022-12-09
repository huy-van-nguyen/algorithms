import unittest


def class_photos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()
    diff = red_shirt_heights[0] - blue_shirt_heights[0]
    for i in range(len(red_shirt_heights)):
        if (red_shirt_heights[i] - blue_shirt_heights[i]) * diff <= 0:
            return False
    return True


class TestProgram(unittest.TestCase):
    def test_class_photos(self):
        red_shirt_heights = [5, 8, 1, 3, 4]
        blue_shirt_heights = [6, 9, 2, 4, 5]
        expected = True
        actual = class_photos(red_shirt_heights, blue_shirt_heights)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
