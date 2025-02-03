from random import randint


def roll_dice(*dice, samples=1_000_000):
    total_count = {}
    for _ in range(0,samples):
        sum = 0
        for item in dice:
            rand_i = randint(1, item)
            sum += rand_i
        if sum not in total_count:
            total_count[sum] = 1
        else:
            total_count[sum] += 1
    total_count = dict(sorted(total_count.items()))

    print('Outcome Probability')
    for roll, count in total_count.items():
        print(f'{roll}\t{count/samples*100 :0.2f}%')


# commands used in solution video for reference
if __name__ == '__main__':
    roll_dice(4, 6, 6)
    roll_dice(4, 6, 6, 20)
