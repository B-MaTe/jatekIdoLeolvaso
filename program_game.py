import time
import os
from os import path
import json
import subprocess
from math import ceil



#########################
#  JATEK IDO LEOLVASAS  #
#########################
PATH = os.getcwd() + '\\'
timestr = time.strftime("%Y_%m_%d")
extension = '.json'
FULLPATH = PATH + timestr + extension


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
        loop()

    if not path.exists(FULLPATH):
        create_file()
        handle_file()
        loop()

def loop():
    active = 1
    while active:
        while True:
            p = subprocess.run(['tasklist'], stdout=subprocess.PIPE, shell=True)
            if b'VALORANT.exe' in p.stdout or b'csgo.exe' in p.stdout or b'javaw.exe' in p.stdout or b'FortniteLauncher.exe' in p.stdout or b'PUBGLite.exe' in p.stdout:
                print('START!')
                start = time.time()
                break
        while True:
            p = subprocess.run(['tasklist'], stdout=subprocess.PIPE, shell=True)
            if b'VALORANT.exe' not in p.stdout and b'csgo.exe' not in p.stdout and b'javaw.exe' not in p.stdout and b'FortniteLauncher.exe' not in p.stdout and b'PUBGLite.exe' not in p.stdout:
                print('END!')
                end = time.time()
                handle_file()
                break
        lasted_time = end - start
        lasted_time = int(ceil(lasted_time))
        with open(FULLPATH, 'w') as f:
            time_spent_gaming = (lasted_time // 60) + value
            json.dump(time_spent_gaming, f)
main()

