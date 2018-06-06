from aupyom import Sound
from aupyom import Sampler
import time

keys_file = "sounds/1901_keys.mp3"

keys = Sound.from_file(keys_file)
sampler = Sampler()

t_end = time.time() + 60 * 1

sampler.play(keys)
print('played')

while time.time() < t_end:
    # do whatever you do

    print('hee')



