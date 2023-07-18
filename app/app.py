import os
import time
import schedule
import requests
from loguru import logger


PUSH_INTERVAL = int(os.getenv("PUSH_INTERVAL"))
PUSH_URL = os.getenv("PUSH_URL")


def main():
  try:
    logger.info("Pinging " + PUSH_URL)
    response = requests.get(PUSH_URL)
  except Exception as e:
    logger.error("Error updating sensor. \n" + str(e))



if __name__ == "__main__":
  logger.info("Starting agent")
  logger.info("Sensor URL: " + PUSH_URL) 
  #Calling main at startup
  main()   
  schedule.every(PUSH_INTERVAL).seconds.do(main)
  
  while True:
    schedule.run_pending()
    time.sleep(1)
