import time
from datetime import datetime as dt

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours ....")
    else:
        print("Fun hours")
    time.sleep(2)
