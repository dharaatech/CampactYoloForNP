import cv2
import numpy as np
from ..imageProcessing import preprocess


INFO = "[INFO] : "
ERROR = "[ERROR] : "

"""
    *** HORIZON DETECTION.
    {
         :
        
    }
     
"""

class HorisonDetection:
    
    def readVideo(self, image):

        vid = cv2.VideoCapture(image)
        width = int(vid.get(3))
        height = int(vid.get(4))
        size = (width, height)
        
        # cv2.VideoWriter("name.avi", cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

        while True:
            ret, realImage = vid.read()
            if realImage is not None:
                frames = self.grayScale(realImage)
                frames = self.threshold(frames)
                frames = cv2.Laplacian(frames, cv2.CV_64F)
                frames = np.uint8(frames)
                frames = self.canny(frames)
                self.detectLinesFoVideos(realImage, frames)
                # frames = self.opening(frames)                
                if ret:
                    cv2.imshow("frame", realImage)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                elif ret == False:
                    print("Video Finished.")
                    exit()
        vid.release()
        cv2.destroyAllWindows()
    
    def detectLinesFoVideos(self, realimage, image):
        lines = cv2.HoughLines(image,1,np.pi/180,200)
        try:
            for line in lines:
                for rho,theta in line:
                        a = np.cos(theta)
                        b = np.sin(theta)
                        x0 = a*rho
                        y0 = b*rho
                        x1 = int(x0 + 10000*(-b))
                        y1 = int(y0 + 5000*(a))
                        x2 = int(x0 - 10000*(-b))
                        y2 = int(y0 - 5000*(a))

                        return cv2.line(realimage,(x1,y1),(x2,y2),(0,0,255),2)
        except Exception as e:
            print("{} {}".format(ERROR, e))


# HorisonDetection("../../images/PeriscopeBest.mp4")




