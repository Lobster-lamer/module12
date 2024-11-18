from runner_edited import Runner, Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        _walker = Runner("Pantera")
        for _ in range(10):
            _walker.walk()
        self.assertEqual(_walker.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        _runner = Runner("Forest")
        for _ in range(10):
            _runner.run()
        self.assertEqual(_runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        _walker = Runner("Pantera")
        _runner = Runner("Forest")
        for _ in range(10):
            _walker.walk()
            _runner.run()
        self.assertNotEqual(_walker.distance, _runner.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.usein = Runner("Усейн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1_usein_nik(self):
        tournament = Tournament(90, self.usein, self.nik)
        tournament_result = tournament.start()
        self.all_results.append(tournament_result)
        self.assertEqual(tournament_result[max(tournament_result.keys())], "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        tournament_result = tournament.start()
        self.all_results.append(tournament_result)
        self.assertEqual(tournament_result[max(tournament_result.keys())], "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
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
