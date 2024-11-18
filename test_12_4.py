from Human_move_test import Runner
import unittest
import logging
import os


class RunnerTest(unittest.TestCase):

    logging.basicConfig(handlers=[logging.FileHandler("runner_tests.log", 'w', 'utf-8')],
                        level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] (%(filename)s).%(funcName)s(%(lineno)d): %(message)s")


    def test_walk(self):
        try:
            _walker = Runner("Pantera", -5)
            for _ in range(10):
                _walker.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(_walker.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            _runner = Runner(322)
            for _ in range(10):
                _runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(_runner.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        _walker = Runner("Pantera")
        _runner = Runner("Forest")
        for _ in range(10):
            _walker.walk()
            _runner.run()
        self.assertNotEqual(_walker.distance, _runner.distance)
