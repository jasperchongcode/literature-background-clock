from change_background import set_current_time
import schedule
import time

# def doing():
#     try:
#         set_current_time()
#     except:
#         pass
print('starting')
set_current_time()

schedule.every().minute.at(':00').do(set_current_time)
while True:
    schedule.run_pending()
    time.sleep(.1)