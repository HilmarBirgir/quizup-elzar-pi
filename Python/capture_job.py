import picamera

import os
import threading

camera = picamera.PiCamera()
picture_path = '/canteen_image/'
seconds_between_captures = 5

def capture():
    file_name = os.getcwd() + picture_path + 'image.jpg'
    camera.capture(file_name)
    print('captured image: ' + file_name)

def run_capture_job():
    capture()
    threading.Timer(seconds_between_captures, run_capture_job).start()

run_capture_job()
