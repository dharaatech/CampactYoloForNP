import os
import cv2
import numpy as np


INFO = "\033[92m{}\033[00m".format("[INFO] : ")
ERROR = "\033[91m{}\033[00m".format("[ERROR] : ")


class Preprocess:


    def __init__(self, imageName):

        self.imageName = imageName
        if type(self.imageName) == str:
            if not os.path.exists(self.imageName):
                print("Invalid path")
                exit()
    
    def __le__(self) -> bool:
        
        if len(self.image) > 1:
            return True
        return False
    
    def opening(self, image, kernel=np.ones((5, 5), np.uint8), iterations=3, bordertype=cv2.BORDER_DEFAULT):

        open_ = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations)
        return open_
    
    def threshold(self, image):
        _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return thresh
    
    def erode(self, image, kernel=np.ones((5, 5), np.uint8), dst=None, border=cv2.BORDER_DEFAULT, iterations=3):
        """
            @Param image : image to be eroded.
            @Param kernel : A structuring element used for erosion. If element = Mat(), a 3 x 3 rectangular structuring element is used. Kernel can be created using getStructuringElement.
            @Param dst : It is the output image of the same size and type as src.
            @Param border : It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc.
            @Param iterations : It is number of times erosion is applied.

            @return : returns an image.
        """
        return cv2.erode(image, kernel=kernel, borderType=border, iterations=iterations)

    def dilate(self, image, kernel=np.ones((5, 5), np.uint8), dst=None, border=cv2.BORDER_DEFAULT, iterations=3):
        """
            @Param image : image to be eroded.
            @Param kernel : A structuring element used for erosion. If element = Mat(), a 3 x 3 rectangular structuring element is used. Kernel can be created using getStructuringElement.
            @Param dst : It is the output image of the same size and type as src.
            @Param border : It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc.
            @Param iterations : It is number of times erosion is applied.

            @return : returns an image.
        """
        return cv2.erode(image, kernel=kernel, borderType=border, iterations=iterations)
    
    def canny(self, image):
        return cv2.Canny(image, 50, 50, apertureSize=3)

    def grayScale(self, image):
        try:
            if image.ndim != 2:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                return gray
            return image
        except Exception as e:
            print(">", e)
            pass
    
    def bitwiseNot(self, image):

        return cv2.bitwise_not(image)
    
    def gblur(self, image, kernel=(5, 5), bordertype=cv2.BORDER_DEFAULT):
        return cv2.GaussianBlur(image, kernel, bordertype)

    def filter2d(self, image, kernel=np.ones((5, 5), np.uint8)):
        kernel = np.ones((5,5),np.float32)/25
        dst = cv2.filter2D(image,-1,kernel)

        return dst

        
   
def resizeImage(image : list, width : int = 256, height : int = 256):

    width_ = abs(width)
    height_ = abs(height)

    try:
        resize = cv2.resize(image, (width_, height_))
    except Exception as e:
        print("{} : {}".format(ERROR, e))
        exit()

    return resize

