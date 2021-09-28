#from google.colab.patches import cv2_imshow
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file = askopenfilename()

x=file

img = cv2.imread(x,1)
cv2.imshow("Original Picture", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grey Picture",img)

img_invert = cv2.bitwise_not(img_gray)
#cv2.imshow("Inverted Picture", img_invert)

img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
#cv2.imshow("Smooth Picture", img_smoothing)

def dodgeV2(x, y):
	return cv2.divide(x, 255 - y, scale=256)

final_img = dodgeV2(img_gray, img_smoothing)
cv2.imshow("Pencil Sketch", final_img)
cv2.waitKey(0)