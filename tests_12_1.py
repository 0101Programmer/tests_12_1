import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        some_runner = runner.Runner('Bunny')
        for i in range(1, 11):
            some_runner.walk()
        self.assertEqual(some_runner.distance, 50)

    def test_run(self):
        some_runner = runner.Runner('Bilbo')
        for i in range(1, 11):
            some_runner.run()
        self.assertEqual(some_runner.distance, 100)

    def test_challenge(self):
        first_runner = runner.Runner('Joni')
        second_runner = runner.Runner('Threes')
        for i in range(1, 11):
            first_runner.run()
        for i in range(1, 11):
            second_runner.walk()
        self.assertNotEqual(first_runner.distance, second_runner.distance)








