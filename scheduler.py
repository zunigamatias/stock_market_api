import time
 
import schedule

from datetime import datetime
from script import stock_job

def basic_job():
    print(f'Job started at: {datetime.now()}')
    
schedule.every().minute.do(basic_job)

schedule.every().day.at("01:11").do(stock_job)
# schedule.every().minute.do(stock_job)

while True:
    schedule.run_pending()
    time.sleep(1)
