# internet is back notifier
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import requests
import time
import pygame

def alarm():
   pygame.mixer.init()
   pygame.mixer.music.load("ohmygah.mp3")
   pygame.mixer.music.play()

while True:
    try:
        print('Trying to get https://www.google.com')
        resp = requests.get('https://www.google.com/')
        print('\nPage loaded')
        for i in range(5):
           alarm()
           time.sleep(2)
        break
    except:
        time.sleep(0.7)
        continue
