from runner_edited import Runner, Tournament
# from pprint import pprint
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usein = Runner("Усейн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    def test_1_usein_nik(self):
        tournament = Tournament(90, self.usein, self.nik)
        tournament_result = tournament.start()
        self.all_results.append(tournament_result)
        self.assertEqual(tournament_result[max(tournament_result.keys())], "Ник")

    def test_2_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        tournament_result = tournament.start()
        self.all_results.append(tournament_result)
        self.assertEqual(tournament_result[max(tournament_result.keys())], "Ник")

    def test_3_everyone(self):
        tournament = Tournament(90, self.usein, self.andrey, self.nik)
        tournament_result = tournament.start()
        self.all_results.append(tournament_result)
        self.assertEqual(tournament_result[max(tournament_result.keys())], "Ник")

    @classmethod
    def tearDownClass(cls):
        # pprint(cls.all_results)
        for tournament_result in cls.all_results:
            print(tournament_result)


if __name__ == "__main__":
    unittest.main()