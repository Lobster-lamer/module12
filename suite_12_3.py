import unittest
from test_12_3 import RunnerTest, TournamentTest


total_test = unittest.TestSuite()
total_test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
total_test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

unittest.TextTestRunner(verbosity=2).run(total_test)
