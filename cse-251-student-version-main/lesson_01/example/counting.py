"""
Course: CSE 251
Lesson Week: 01
File: week01-counting.py
Author: Brother Comeau
"""

import time
import threading
from cse251 import *

global_count = 0

THREADS = 4
COUNT = 100

def count(lock):
    global global_count
    for i in range(COUNT):
        lock.acquire()
        global_count += 1
        lock.release()

def main():
    threads = []

    global global_count
    global_count = 0

    lock = threading.Lock()
    
    for i in range(THREADS):
        t = threading.Thread(target=count, args=(lock,))
        threads.append(t)
        
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f'{global_count = }')
    
    
if __name__ == '__main__':
    main()