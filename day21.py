from aocd import get_data
import re
import functools

mx = r'^[a-zA-Z0-9\\:]*\\day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """Player 1 starting position: 4
Player 2 starting position: 8"""

class Die:
    def __init__(self):
        self.val = 1
        self.num_rolls = 0

    def roll(self):
        rolls = self.val + (self.val+1)%100 + (self.val+2)%100
        self.val += 3
        if self.val > 100:
            self.val %= 100
        self.num_rolls += 3
        return rolls

class Player:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.score = 0

    def move(self, dice_roll):
        pos = self.pos - 1
        pos += dice_roll
        pos %= 10
        pos += 1
        self.pos = pos
        self.score += pos
        if self.score >= 1000:
            return True
        else:
            return False


def play_game(start_pos_1, start_pos_2):
    p1 = Player(start_pos_1)
    p2 = Player(start_pos_2)
    d = Die()
    while True:
        roll = d.roll()
        won = p1.move(roll)
        if won:
            losing_score = p2.score
            num_rolls = d.num_rolls
            break
        roll = d.roll()
        won = p2.move(roll)
        if won:
            losing_score = p1.score
            num_rolls = d.num_rolls
            break
    final_score = losing_score*num_rolls
    return final_score


def part_one(input_data):
    p1, p2 = [int(j[-1]) for j in input_data.split('\n')]
    answer = play_game(p1,p2)
    print(answer)

@functools.cache
def play_game_part_two(positions, scores, player=0):
    probability_of_rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    positions = list(positions)
    scores = list(scores)
    wins = [0, 0]

    start_pos = positions[player]
    start_score = scores[player]

    for roll, universes in probability_of_rolls.items():
        positions[player] = (start_pos + roll) % 10 or 10
        scores[player] = start_score + positions[player]
        if scores[player] >= 21:
            wins[player] += universes
        else:
            more_wins = play_game_part_two(tuple(positions), tuple(scores), (player + 1) % 2)
            for idx, count_of_wins in enumerate(more_wins):
                wins[idx] += universes * count_of_wins
    return wins

def part_two(input_data):
    positions = tuple([int(j[-1]) for j in input_data.split('\n')])
    scores = (0,0)

    wins = play_game_part_two(positions, scores)
    print(wins)


# part_one(input_data)
part_two(input_data)