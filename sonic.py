from psonic import *
import random

F6 = 89
Ds6 = 87
Cs6 = 85

use_synth(SAW)

@in_thread
def octave_six():
    # group_00_oct6
    sleep(0.23)
    sleep(0.23)
    play(F6)
    sleep(0.23)
    play(Ds6)
    sleep(0.23)
    play(Cs6)
    sleep(0.23)
    play(C6)
    sleep(0.23)
    play(Cs6)
    sleep(0.23)
    play(C6)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    play(C6)
    sleep(0.23)
    play(Cs6)
    sleep(0.23)
    play(Ds6)
    sleep(0.23)
    play(Cs6)
    sleep(0.23)
    play(C6)
    sleep(0.23)
    # group_01_oct6
    sleep(0.23)
    sleep(0.23)
    play(C6)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    play(F6)
    sleep(0.23)
    play(Ds6)
    sleep(0.23)
    play(Cs6)
    sleep(0.23)
    play(C6)
    sleep(0.23)
    play(Cs6)
    sleep(0.23)
    play(C6)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    play(C6)
    sleep(0.23)
    play(Cs6)
    sleep(0.23)

@in_thread
def octave_five():
    # group_00_oct5
    play(As5)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    play(As5)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    # group_01_oct5
    play(Gs5)
    play(F5)
    sleep(0.23)
    play(F5)
    play(As5)
    play(F5)
    play(As5)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)
    play(As5)
    play(F5)
    sleep(0.23)
    play(F5)
    sleep(0.23)
    play(F5)

@in_thread
def octave_three():
    # group_00_oct3
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    play(F3)
    sleep(0.23)

@in_thread
def octave_two():
    # group_00_oct2
    play(As2)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    play(F2)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    # group_01_oct2
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    play(As2)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)
    play(F2)
    sleep(0.23)
    sleep(0.23)
    sleep(0.23)

octave_six()
octave_five()
octave_three()
octave_two()
