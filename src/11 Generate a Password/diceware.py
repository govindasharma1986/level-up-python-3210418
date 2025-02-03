import re
import secrets


def generate_passphrase(num_words, filename='diceware.wordlist.asc'):
    dice_pattern = re.compile(r"^(\d+)\t(.*)$")
    dice_rolls = {}
    with open(filename, 'r') as fhandler:
        while line := fhandler.readline():      
            if match := re.match(dice_pattern, line):
                groups = match.groups()
                dice_rolls[groups[0]] = groups[1].strip()

    roll = ''
    words = []
    for _ in range(num_words):
        roll = roll_dice(6,6,6,6,6)
        words.append(dice_rolls[roll])
    return ' '.join(words)


def roll_dice(*dices) -> str:
    roll = ''
    for sides in dices:
        side = secrets.randbelow(sides) + 1
        roll += str(side)
    return roll


# commands used in solution video for reference
if __name__ == '__main__':
    print(generate_passphrase(7))
    print(generate_passphrase(7))
