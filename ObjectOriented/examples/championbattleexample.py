import random


# TODO: add energy
# TODO: in calculate_real_dmg function add a random chance to cast special skill
# special skill uses energy

class Stats:
    def __init__(self, base_stats):
        self.hp = base_stats.hp
        self.dmg = base_stats.dmg
        self.crit_chance = base_stats.crit_chance
        self.crit_factor = base_stats.crit_factor

    def display(self):
        for stat, value in self.__dict__.items():
            if not stat.startswith('__'):
                print('{}: {}'.format(stat, value))


class StatsSpartan:
    hp = 1300
    dmg = 40
    crit_chance = 0.2
    crit_factor = 3


class StatsSamurai:
    hp = 900
    dmg = 55
    crit_chance = 0.5
    crit_factor = 2


class StatsCrusader:
    hp = 1500
    dmg = 52
    crit_chance = 0.05
    crit_factor = 1.5


class Champion:
    def __init__(self, name, base_stats):
        self.alive = None
        self.base_stats = base_stats

        self.name = name
        self.stats = None

        self._spawn()

    def _set_stats(self):
        self.stats = Stats(self.base_stats)

    def _spawn(self):
        self.alive = True
        self._set_stats()

    def respawn(self):
        self._spawn()

    def display_stats(self):
        print('Champion: {}'.format(self.name))
        self.stats.display()

    def attack(self, champion_victim):
        real_dmg = self.calculate_real_dmg()
        champion_victim.receive_dmg(
            real_dmg
        )

    def receive_dmg(self, dmg_taken):
        self.stats.hp -= dmg_taken

        if self.stats.hp <= 0:
            self.die()

    def calculate_real_dmg(self):
        # a number between (0, 1)
        if random.random() <= self.stats.crit_chance:
            # Critical!
            return self.stats.dmg * self.stats.crit_factor

        else:
            return self.stats.dmg

    def die(self):
        self.alive = False


def battle(champion_1, champion_2, info=False):
    if info:
        champion_1.display_stats()
        print('-' * 20)
        champion_2.display_stats()

    if info:
        print('/\\' * 10 + '\n' + 'BATTLE!' * 3 + '\n' + '/\\' * 10)

    while champion_1.alive and champion_2.alive:
        champion_1.attack(champion_2)
        champion_2.attack(champion_1)

    if info:
        champion_1.display_stats()
        print('-' * 20)
        champion_2.display_stats()

    if not champion_1.alive and not champion_2.alive:
        winner = None

    elif not champion_1.alive:
        winner = champion_2

    else:
        winner = champion_1

    if info:
        print('=' * 20)
        if winner:
            print('Winner: {}'.format(winner.name))

        else:
            print('Draw...')

    return winner


def tournament(champ_1, champ_2, number_of_battles=100, info=False):
    results = {
        'draws': 0,
        champ_1.name: 0,
        champ_2.name: 0,
    }

    for round_ in range(1, number_of_battles + 1):
        if info:
            print('#' * 20)
            print('ROUND: {}'.format(round_))

        champ_1.respawn()
        champ_2.respawn()

        winner = battle(champ_1, champ_2, info=info)

        if winner:
            results[winner.name] += 1

        else:
            results['draws'] += 1

    return results


def manager(champions, extended_info=False, number_of_battles=100):
    # Fight them in all combinations
    for index, champ_1 in enumerate(champions):
        # Slice second iteration to avoid duplicate tournaments
        for champ_2 in champions[index + 1:]:
            # Skip against itself
            # if champ_1 == champ_2:
            #     continue

            results = tournament(
                champ_1,
                champ_2,
                number_of_battles=number_of_battles,
                info=extended_info,
            )

            print('~' * 50)
            print('{} VS {}'.format(champ_1.name, champ_2.name))
            print(results)


if __name__ == '__main__':
    # Define set up
    CHAMPIONS_SCHEMA = {
        'Spartan': StatsSpartan,
        'Samurai': StatsSamurai,
        'Crusader': StatsCrusader,
    }

    EXTENDED_INFO = False
    ROUNDS_PER_BATTLE = 3000

    # Init champion container
    CHAMPIONS = []

    for champ_name, champ_stats in CHAMPIONS_SCHEMA.items():
        CHAMPIONS.append(
            Champion(
                name=champ_name,
                base_stats=champ_stats,
            )
        )

    manager(
        CHAMPIONS,
        extended_info=EXTENDED_INFO,
        number_of_battles=ROUNDS_PER_BATTLE,
    )
