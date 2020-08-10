# EXERCISE 7
# Healthy Programmer
# This will remind
# Water-water.mp3(3.5 liters) - give input drank - log time stamp - every 40 mins
# Eyes-eyes.mp3 (30 mins) - input eydone - log time stamp
# Physical activity-physical.mp3 (45 mins) - input exdone - log time stamp
# 9am - 5pm
# How to play mp3
# If times clash wait for the other.
# Use pygame to play audio.

                    # SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
   mixer.init()
   mixer.music.load(file)
   mixer.music.play()
   while True:
       imput_of_user = input()
       if imput_of_user == stopper:
           mixer.music.stop()
           break

def log_now(msg):
    with open("MyLogs.txt", "a") as f:
        f.write(f"{msg},{datetime.now()}\n")

if __name__ == '__main__':
    musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 10
    exsecs =  15
    eyessecs = 45

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time. Enter 'drank' to stop the alarm.")
            musiconloop("water.mp3", "drank")
            init_water = time()
            log_now("Drank water at")

        if time() - init_eyes > eyessecs:
            print("Eye Exercise Time. Enter 'doneeyes' to stop the alarm.")
            musiconloop("water.mp3", "doneeyes")
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop("water.mp3", "donephy")
            init_exercise = time()
            log_now("Physical Activity Done at")
