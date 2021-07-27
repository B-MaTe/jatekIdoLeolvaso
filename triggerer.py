import datetime as dt
import os
from subprocess import Popen
import time

PATH = os.getcwd() + '\\'
timestr = time.strftime("%Y_%m_%d")
extension = '.json'
FULLPATH = PATH + timestr + extension
CMDPATH = PATH + 'triggerer.bat'



while True:
    if os.path.exists(FULLPATH):    
        with open(FULLPATH) as f:
            value = f.read()
            value = int(value)
            if value >= 150:
                Popen(CMDPATH)
                break
    now = dt.datetime.now()
    if now.hour > 20 or now.hour < 7:
        Popen(CMDPATH)
        break
    