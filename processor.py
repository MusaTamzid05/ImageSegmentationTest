import cv2
import numpy as np


class Processor:

    def __init__(self):
        pass

    def process(self , image , min_range1 , max_range1 , min_range2 , max_range2):

        hsv_image = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv_image , np.array(min_range1), np.array(max_range1))
        mask2 = cv2.inRange(hsv_image , np.array(min_range2), np.array(max_range2))

        return mask1 , mask2


