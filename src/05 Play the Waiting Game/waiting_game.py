import time
import random

def waiting_game():
    target = random.randint(2, 4)
    print(f'Your target time is {target} seconds')
    
    input('--- Press Enter to Begin ---')
    t_start = time.time()
    
    input(f'... Press Enter again after {target} seconds ...')
    t_end = time.time()
    
    t_elapsed = float("{:.3f}".format(t_end - t_start))
    print(f'Elapsed time: {t_elapsed} seconds')
    
    t_diff = float("{:.3f}".format(target - t_elapsed))
    if t_diff > 0:
        print(f'({abs(t_diff)} seconds too fast)')
    
    elif t_diff < 0:
        print(f'({abs(t_diff)} seconds too slow)')
    
    else:
        print(f'You are right on time')


# commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()
