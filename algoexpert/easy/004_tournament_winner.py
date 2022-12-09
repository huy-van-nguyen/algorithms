import unittest


def tournament_winner(competitions, results):
    if len(competitions) != len(results):
        return None
    dict = {}
    winner = None
    points = 0
    for i in range(len(competitions)):
        if results[i] != 0:
            won = competitions[i][0]
        else:
            won = competitions[i][1]
        if won in dict:
            dict[won] += 3
        else:
            dict[won] = 3
        if dict[won] > points:
            points = dict[won]
            winner = won
    return winner


class TestProgram(unittest.TestCase):
    def test_tournament_winner(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = 'Python'
        actual = tournament_winner(competitions, results)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
