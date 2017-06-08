import os
import sys

#script audio.py

import wave
import math
import binascii
import winsound
import pygame

pygame.mixer.init()
pygame.mixer.Sound('DCNE.wav').play()

while pygame.mixer.get_busy():
  pass
