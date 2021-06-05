"""
Tutorial:https://youtu.be/nv7ARUjpzkE
"""

import numpy as np
import cv2
import pyautogui

screen_size = (1920,1080)

frames_per_second = 20.0

video_codec = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('out.avi',video_codec,frames_per_second,screen_size)

while True:
    image = pyautogui.screenshot()

    frame = np.array(image)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame)

output.release()
cv2.destroyAllWindows()


