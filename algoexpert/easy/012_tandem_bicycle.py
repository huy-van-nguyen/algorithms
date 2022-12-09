import unittest


def tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest):
    red_shirt_speeds.sort()
    blue_shirt_speeds.sort(reverse=True) if fastest else blue_shirt_speeds.sort()
    max_min = 0
    for i in range(len(red_shirt_speeds)):
        max_min += max(red_shirt_speeds[i], blue_shirt_speeds[i])

    return max_min


class TestProgram(unittest.TestCase):
    def test_tandem_bicycle(self):
        red_shirt_speeds = [5, 5, 3, 9, 2]
        blue_shirt_speeds = [3, 6, 7, 2, 1]
        fastest = True
        expected = 32
        actual = tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()