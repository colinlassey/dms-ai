from picamera2 import Picamera2
import time

cam = Picamera2()
cam.configure(cam.create_preview_configuration())
cam.start()

print("camera initialized")

cam.capture_file("test.jpg")
print("image captured successfully")

cam.stop()
