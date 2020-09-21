import pygame
import time
import pygame.midi

pygame.midi.init()
player = pygame.midi.Output(0)


player.set_instrument(1, 0)
player.set_instrument(1, 1)
player.set_instrument(126, 2)
player.set_instrument(101, 3)

notes={'c': 24, 'C': 25, 'd': 26, 'D': 27,
       'e': 28, 'f': 29, 'F': 30, 'g': 31,
       'G': 32, 'a': 33, 'A': 34, 'b': 35, '-':0}

channel0 = ('--d---------------d---------------d---------------d---------------d-----------', 0, 5)
channel1 = ('dd--a--G-g-f-dfgcc--a--G-g-f-dfg----a--G-g-f-dfg----a--G-g-f-dfgdd--a--G-g-f-d', 1, 4)
channel2 = ('--------------------------------bb--------------AA----------------------------', 2, 3)

active_channel = [channel0 , channel1]

def play(note, channel, octave):
    player.note_on(note + (12*octave), 64, channel)
    time.sleep(0.15)

def stepPlay(active_channel, note_number):
    num_silence = 0
    for channel in active_channel:
        note = channel[0][note_number]
        if(note != '-'):
            play(notes[note], channel[1], channel[2])
        else:
            num_silence += 1
        if(num_silence == len(active_channel)):
            num_silence = 0
            time.sleep(0.15)


for i in range(len(channel0[0])):
    stepPlay(active_channel, i)

del player
