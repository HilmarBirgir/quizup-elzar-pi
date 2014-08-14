import picamera

import time
import datetime
import threading

camera = picamera.PiCamera()

def capture():
    file_name = '/home/pi/Desktop/Projects/quizup-elzar/images' + time_stamp() + '.jpg'
    camera.capture(file_name)
    print('captured image: ' + file_name)
    upload(file_name)

def time_stamp():
    time_in_seconds = time.time()
    time_stamp = datetime.datetime.fromtimestamp(time_in_seconds).strftime('%Y-%m-%d %H:%M:%S')

    return time_stamp

def capture_and_upload():
    capture()
    threading.Timer(1800, capture_and_upload).start()


capture_and_upload()