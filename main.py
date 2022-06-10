from picamera import PiCamera
from time import sleep


camera = PiCamera()
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous('images/img_{counter:010d}.jpg'):
  sleep(1)