import os
import time
import schedule
import requests
from loguru import logger


PUSH_INTERVAL = int(os.getenv("PUSH_INTERVAL"))
PUSH_URL = os.getenv("PUSH_URL")




if __name__ == "__main__":
  logger.info("Starting")
