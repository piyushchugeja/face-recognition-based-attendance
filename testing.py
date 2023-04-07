import threading
import time
from datetime import datetime
from operations import *
def check_month_change():
    current_month = datetime.now().strftime('%B')
    while True:
        time.sleep(3600) # wait for an hour before checking again
        if datetime.now().strftime('%B') != current_month:
            send_monthly_attendance(current_month)
            current_month = datetime.now().strftime('%B')
# start the background task in a separate thread
t = threading.Thread(target=check_month_change)
t.daemon = True
t.start()