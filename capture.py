import picamera

import os
import datetime
import threading

camera = picamera.PiCamera()
picture_path = '/canteen_image/'

def capture():
    file_name = os.getcwd() + picture_path + 'image.jpg'
    camera.capture(file_name)
    print('captured image: ' + file_name)

def run_capture_job():
    capture()
    threading.Timer(5, capture).start()

run_capture_job()
