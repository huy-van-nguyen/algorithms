import unittest


def merge_overlapping_intervals(intervals):
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda x: x[0])
    array = []
    prev_interval = intervals[0]
    prev_start = prev_interval[0]
    prev_end = prev_interval[len(prev_interval)-1]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        start = interval[0]
        end = interval[len(interval)-1]
        overlap = [prev_start, prev_end, start, end]
        overlap.sort()
        if prev_end != start and ((prev_start in overlap[:2] and prev_end in overlap[:2]) or (start in overlap[:2] and end in overlap[:2])):
            array.append([prev_start, prev_end])
            prev_start = start
            prev_end = end
        else:
            prev_start = overlap[0]
            prev_end = overlap[3]
    array.append([prev_start, prev_end])
    return array


class TestProgram(unittest.TestCase):
    def test_merge_overlapping_intervals(self):
        intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
        expected = [[1, 2], [3, 8], [9, 10]]
        actual = merge_overlapping_intervals(intervals)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
