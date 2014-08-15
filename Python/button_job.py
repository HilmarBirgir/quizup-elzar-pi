import serial
import requests

ser = serial.Serial('/dev/ttyACM0', 9600)

def post_lunch_is_ready():
    requests.post("http://quizup-elzar.herokuapp.com/lunch")

def run_button_job():

    button_pressed = 0
    button_fired = 0

    while True:
        readline = ser.readline()[0]

        if readline.strip():
            readline_int = int(readline)

            if button_pressed != readline_int:
                button_fired = 0

            button_pressed = readline_int

        if button_pressed and button_fired == 0:
            button_fired = 1
            print 'Button Pressed!'

run_button_job()