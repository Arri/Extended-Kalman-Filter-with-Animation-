####################################
# Video-stream to remote observe the IMU
# Author: Arasch U Lagies
# Date Created: 6/30/2020
# Last Update:
#
# Call
####################################
import os 
import cv2
import argparse
import time

WIDTH = 640
HEIGHT = 480
FPS = 30
CAMERA = 0

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--width", default=WIDTH, 
                help="Width of the input image. Default is {}".format(WIDTH))
ap.add_argument("-e", "--height", default=HEIGHT,
                help="Height of the input image. Default is {}".format(HEIGHT))
ap.add_argument("-f", "--fps", default=FPS,
                help="Framerate of the camera. Default is {}".format(FPS))
ap.add_argument("-i", "--id", default=CAMERA,
                help="ID of the attached camera. Default is {}".format(CAMERA))
args = ap.parse_args()

class video:
    def __init__(self, width=args.width, height=args.height, fps=args.fps, id=args.id):
        ''' Configure the camera '''
        self.width = width
        self.height = height
        self.fps = fps
        self.camera = cv2.VideoCapture(id)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.camera.set(cv2.CAP_PROP_FPS, self.fps)
        print("[INFO] Camera is warming up...")
        time.sleep(1)
        if self.camera.isOpened():
            self.grabbed, self.frame = self.camera.read()
        else:
            self.grabbed = False
            raise Exception("[ERROR] Could not open the camera.")

    def get(self):
        while self.grabbed:
            self.frame180 = cv2.rotate(self.frame, cv2.ROTATE_180)
            cv2.imshow("life stream", self.frame180)
            self.grabbed, self.frame = self.camera.read()
            key = cv2.waitKey(20)
            if key == 27:
                break

    def shut(self):
        fps_get = self.camera.get(cv2.CAP_PROP_FPS)
        print(f"[INFO] The camera speed was {fps_get}fps.")
        print("[INFO] Closing the camera.")
        self.camera.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    stream = video()
    stream.get()
    stream.shut()


