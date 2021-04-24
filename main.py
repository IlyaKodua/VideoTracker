# This is a sample Python script.


import cv2

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Tracker as Tr
import  numpy as  np
print(1)

if __name__ == '__main__':

	img1 = cv2.imread("examples/ex1.png")
	img2 = cv2.imread("examples/ex2.png")


	track = Tr.Tracker(img1, img2)
	df = track.diff()
	cv2.imshow("1", df)
	cv2.waitKey(0)
	print("end")

