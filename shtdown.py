import time
from threading import Thread
import os


a = 1
def executer():
    global a
    while True:
        psw = input("Jelszo: ")
        if psw.lower() == 'mateakiraly123':
            a = 2
            break


def timer():
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        if counter > 30 and a != 2:
            #os.system("shutdown /p /f")
            print('asd')
        if a == 2:
            break

t2 = Thread(target=executer).start()
t1 = Thread(target=timer).start()


        
    
    