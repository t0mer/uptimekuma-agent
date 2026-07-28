import os
import sys
import time
import schedule
import requests
from loguru import logger


PUSH_URL = os.getenv("PUSH_URL", "").strip()
PUSH_INTERVAL = int(os.getenv("PUSH_INTERVAL", "50"))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))


def main():
  try:
    logger.info("Pinging " + PUSH_URL)
    response = requests.get(PUSH_URL, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    logger.info("Push succeeded ({})".format(response.status_code))
  except Exception as e:
    logger.error("Error updating sensor. \n" + str(e))



if __name__ == "__main__":
  logger.info("Starting agent")
  if not PUSH_URL:
    logger.error("PUSH_URL is not set. Exiting.")
    sys.exit(1)
  logger.info("Sensor URL: " + PUSH_URL)
  #Calling main at startup
  main()
  schedule.every(PUSH_INTERVAL).seconds.do(main)

  while True:
    schedule.run_pending()
    time.sleep(1)
