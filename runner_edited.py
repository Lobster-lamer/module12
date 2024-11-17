class Runner:
    def __new__(cls, name, speed=5):
        if speed>0:
            return super().__new__(cls)

    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
            for _ in range(len(self.participants)):
                participants_distances = list(map(lambda participant: participant.distance, self.participants))
                fastest_participant = self.participants[participants_distances.index(max(participants_distances))]
                if max(participants_distances) >= self.full_distance:
                    finishers[place] = fastest_participant.name
                    place += 1
                    self.participants.remove(fastest_participant)
        return finishers

if __name__ == "__main__":
    run1 = Runner("bill", 10)
    run2 = Runner("will", 11)
    tournament = Tournament(20, run1, run2)
    tournament_res = tournament.start()
    print(tournament_res)
    print(tournament_res[max(tournament_res.keys())])