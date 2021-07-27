import time
import os
import json
from os import path

PATH = os.getcwd() + '\\'
timestr = time.strftime("%Y_%m_%d")
extension = '.json'
FULLPATH = PATH + timestr + extension

def program():
    global counter
    counter = 0 + value
    while True:
        counter += 1
        time.sleep(60)
        # COUNTING IN MINUTES
        with open(FULLPATH, 'w') as f:
            json.dump(counter, f)



def create_file():
    with open(FULLPATH, 'a') as f:
        starting_zero = 0
        json.dump(starting_zero, f)
        

def handle_file():
    with open(FULLPATH) as f:
        global value
        value = f.read()
        value = int(value)
        return value


def main():
    if  path.exists(FULLPATH):
        handle_file()
        program()

    if not path.exists(FULLPATH):
        create_file()
        handle_file()
        program()


main()