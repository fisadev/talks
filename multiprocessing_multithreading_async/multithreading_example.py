import time
from datetime import datetime
from random import randint
from threading import Thread


info = []
results = []


def generate_info():
    while True:
        time.sleep(1)
        info.append(f"something at {datetime.now()}")
        print("New info added")


def process_info():
    while True:
        time.sleep(1)
        print("Checking for new info")
        if info:
            new_info = info.pop()
            results.append(new_info + "processed")
            print("New info processed")


generator = Thread(target=generate_info)
processor1 = Thread(target=process_info)
processor2 = Thread(target=process_info)

generator.start()
processor1.start()
processor2.start()

generator.join()
