from picamera2 import Picamera2
import time

cam = Picamera2()
cam.start()

print(cam.camera_config)
