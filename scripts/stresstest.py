import logging
import threading
import time
import sys
import requests
import string
import random

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    retunr result_str

def thread_function(name):
    logging.info("V2 launched !!!")
    for i in range(1,10000) :
     r = requests.get(name+"/"+get_random_string(256))
     time.sleep(2)
     
	
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    for i in range(1,10000) :
     x = threading.Thread(target=thread_function, args=(sys.argv[1],))
     
     x.start()
     logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
