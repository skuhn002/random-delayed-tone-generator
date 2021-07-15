from random import randint
import playsound
from time import sleep


def gen_tone(rand_delay=True, my_delay=-1):
    # If rand_delay is False, there will be no time delay before playing the beep
    # my_delay: float - used for setting a consistent delay time (in seconds)
    if rand_delay:
        delay = randint(2, 9) + 3
        print(delay)
        sleep(delay)
    if my_delay != -1:
        delay = my_delay
        print(delay)
        sleep(delay)
    if my_delay != -1 and not rand_delay:
        print("If you wanted a random delay, please don't set my_delay.")
        print("If you wanted to set the delay yourself, please set rand_delay to False")
    playsound.playsound('880Hz_tone.mp3')
