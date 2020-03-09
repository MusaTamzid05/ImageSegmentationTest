import cv2
import numpy as np


class Processor:

    def __init__(self):
        pass

    def process(self , image , min_range , max_range):

        hsv_image = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
        return cv2.inRange(hsv_image , np.array(min_range), np.array(max_range))


