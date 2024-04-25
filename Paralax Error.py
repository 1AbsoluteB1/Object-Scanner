import cv2
import numpy as np
import Object 
h,y,z=Object.Object("Photo_H.jpg")
def Paralax_Error(h,w,min_y):
    angle = np.arctan(272-min_y / 1000)
    h-=(w*np.sin(angle))
    return h
