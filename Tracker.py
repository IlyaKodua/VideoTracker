import cv2
import numpy as np
class Tracker:

    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2
        self.img_diff = 0
        self.blob_arr = []

    def diff(self):
        self.img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2GRAY )
        self.img2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2GRAY )
        df = np.abs(self.img1 - self.img2)

        df = cv2.GaussianBlur(df, (11, 11), 0)
        df = cv2.threshold(df, 127, 255, cv2.THRESH_BINARY)
        df = cv2.erode(df , None, iterations=2)
        self.img_diff= cv2.dilate(df , None, iterations=4)

    def group(self):
        self.img_diff
