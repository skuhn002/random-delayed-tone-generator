from random import randint
import playsound
from time import sleep

delay = randint(2, 9) + 3

sleep(delay)

playsound.playsound('880Hz_tone.mp3')
