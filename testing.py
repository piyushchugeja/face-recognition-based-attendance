import threading
import time
from datetime import datetime

def check_month_change():
    current_month = datetime.now().month
    while True:
        time.sleep(3600) # wait for an hour before checking again
        if datetime.now().month != current_month:
            current_month = datetime.now().month
            # execute your end of month function here

# start the background task in a separate thread
t = threading.Thread(target=check_month_change)
t.daemon = True
t.start()