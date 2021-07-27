import time
import os
from os import path
import json
import subprocess
from math import ceil


################
#    WEB APP   #
################

PATH = os.getcwd() + '\\'
timestr = time.strftime("%Y_%m_%d")
extension = '.json'
WEBFULLPATH = PATH + timestr + '_web' + extension

def create_file_web():
    with open(WEBFULLPATH, 'a') as f:
        starting_zero = 0
        json.dump(starting_zero, f)
        

def handle_file_web():
    with open(WEBFULLPATH) as f:
        global value_web
        value_web = f.read()
        value_web = int(value_web)
        return value_web

def main_web():
    if  path.exists(WEBFULLPATH):
        handle_file_web()
        loop_web()

    if not path.exists(WEBFULLPATH):
        create_file_web()
        handle_file_web()
        loop_web()

def loop_web():
    active = 1
    while active:
        while True:
            p = subprocess.run(['tasklist'], stdout=subprocess.PIPE, shell=True)
            if b'firefox.exe' in p.stdout or b'chrome.exe' in p.stdout or b'opera.exe' in p.stdout or b'msedge.exe' in p.stdout:
                print('START!')
                start_web = time.time()
                break
        while True:
            p = subprocess.run(['tasklist'], stdout=subprocess.PIPE, shell=True)
            if b'firefox.exe' not in p.stdout and b'chrome.exe' not in p.stdout and b'opera.exe' not in p.stdout and b'msedge.exe' not in p.stdout:
                print("END!")
                end_web = time.time()
                handle_file_web()
                break
        lasted_time_web = end_web - start_web
        lasted_time_web = int(ceil(lasted_time_web))
        with open(WEBFULLPATH, 'w') as f:
            time_spent_gaming_web = (lasted_time_web // 60) + value_web
            json.dump(time_spent_gaming_web, f)
main_web()