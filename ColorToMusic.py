#import audio stuff
from aupyom import Sound
from aupyom import Sampler
import time

#import cv stuff
import cv2
import numpy as np
from detect_color_data import detect_color_data

#set up sound files
keys_file = "sounds/1901_keys.mp3"
gtr1_file = "sounds/1901_gtr1.mp3"
triggers_file = "sounds/1901_triggers.mp3"
drumleft_file = "sounds/1901_drumsleft.mp3"

keys = Sound.from_file(keys_file)
gtr1 = Sound.from_file(gtr1_file)
triggers = Sound.from_file(triggers_file)
drumleft = Sound.from_file(drumleft_file)

sampler = Sampler()

t_end = time.time() + 60 * 1

#sampler.play(keys)
sampler.play(gtr1)
sampler.play(triggers)
sampler.play(drumleft)
print('played')

#set up cv
lowerBound_green = np.array([33, 80, 40])
upperBound_green = np.array([102, 255, 255])

lowerBound_red = np.array([0, 100, 100])
upperBound_red = np.array([5, 255, 255])

def SetUpRemoveAddSong(song, color):
    if color == "red":
        w = w_r
    elif color == "green":
        w = w_g

    if song.playing == False:
        if w > 0:
            sampler.play(song)
            print('played song')
    else:
        if w == 0:
            sampler.remove(song)


def SetShifter(song, color):
    if color == "red":
        w = w_r
    elif color == "green":
        w = w_g

    if w > 50:
        w_shifter = 10.0 - float(w)/512.0 * 10.0
        print("song =", song, '  w_shifter=', w_shifter)
        song.pitch_shift = int(w_shifter)


while True:
    x_g, y_g, w_g, h_g = detect_color_data(lowerBound_green, upperBound_green)
    x_r, y_r, w_r, h_r = detect_color_data(lowerBound_red, upperBound_red)

    SetUpRemoveAddSong(triggers, "green") #track keys maps to green
    SetUpRemoveAddSong(gtr1, "red")
    SetUpRemoveAddSong(drumleft, "green")

    print('w_g=', w_g)
    print('w_r=', w_r)

    SetShifter(triggers, "green")
    SetShifter(drumleft, "green")
    SetShifter(gtr1, "red")
