import schedule 
import time

def run_etl():
    # Your ETL logic here
    print("ETL job running...")

schedule.every().day.at("09:00").do(run_etl)

while True:
    schedule.run_pending()
    time.sleep(60)

