from psonic import *
import random

F6 = 89
Ds6 = 87
Cs6 = 85

use_synth(SAW)
@in_thread
def octave_five():
    play(As5)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)
    play(As5)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)
    sleep(0.25)
    play(F5)

@in_thread
def octave_six():
    sleep(0.25)
    sleep(0.25)
    play(F6)
    sleep(0.25)
    play(Ds6)
    sleep(0.25)
    play(Cs6)
    sleep(0.25)
    play(C6)
    sleep(0.25)
    play(Cs6)
    sleep(0.25)
    play(C6)
    sleep(0.25)
    sleep(0.25)
    sleep(0.25)
    play(C6)
    sleep(0.25)
    play(Cs6)
    sleep(0.25)
    play(Ds6)
    sleep(0.25)
    play(Cs6)
    sleep(0.25)
    play(C6)
    sleep(0.6)

octave_five()
octave_six()
