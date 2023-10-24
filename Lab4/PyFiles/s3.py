import datetime
import time

dur = 5
start_time = datetime.datetime.now()

while(datetime.datetime.now() - start_time).seconds < dur:
    current_time = datetime.datetime.now()
    print(f'Текущее время: {current_time.strftime("%H:%M:%S")}')
    time.sleep(1)

print('Все.')