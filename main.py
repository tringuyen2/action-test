import logging
import logging.handlers
import os

import requests
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    city = "Vietnam/Hanoi"
    url = f'https://www.timeanddate.com/weather/{city}'
    r = requests.get(url)
    print(r)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        weather_container = soup.find('div', class_='h2').text
        temperature = soup.find('div', class_='h1').text.strip()
        
        logger.info(f"Weather in {city}: {weather_container}")
        # logger.info(f"Temperature: {temperature}")
    else:
        logger.info("Failed to fetch weather data.")