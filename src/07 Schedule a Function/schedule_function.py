import time
import heapq  # using heapq to solve priority problems
# import playsound


schedules = []
def schedule_function(schedule: float, func: callable, *msg):
    global schedules
    print(f'{func.__name__} scheduled for {time.asctime(time.gmtime(schedule))}')
    # it arranges by 1st element of the tuple
    heapq.heappush(schedules, (schedule, print, msg))


def run_schedule():
    global schedules
    while schedules:
        current_time = time.time()
        if current_time >= heapq.nsmallest(1, schedules)[0][0]:
            temp = heapq.heappop(schedules)
            temp[1](*temp[2])  # print all strings
            # playsound.playsound(r'./rooster.wav')
            print('\a', end='')


# commands used in solution video for reference
if __name__ == '__main__':
    schedule_function(time.time() + 10, print, 'Howdy!')
    schedule_function(time.time() + 2, print, 'Howdy!', 'How are you?')
    run_schedule()
