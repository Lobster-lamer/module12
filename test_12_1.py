from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        _walker = Runner("Pantera")
        for _ in range(10):
            _walker.walk()
        self.assertEqual(_walker.distance, 50)

    def test_run(self):
        _runner = Runner("Forest")
        for _ in range(10):
            _runner.run()
        self.assertEqual(_runner.distance, 100)

    def test_challenge(self):
        _walker = Runner("Pantera")
        _runner = Runner("Forest")
        for _ in range(10):
            _walker.walk()
            _runner.run()
        self.assertNotEqual(_walker.distance, _runner.distance)


if __name__ == "__main__":
    unittest.main()
