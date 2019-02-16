import abc
import logging
import pandas as pd

from ..browser import TimeoutException


logger = logging.getLogger("Airline")


class Airline:
    def __init__(self, name, retry_count):
        self.__name = name
        self.__retry_count = retry_count

    @property
    def name(self):
        return self.__name

    @property
    def retry_count(self):
        return self.__retry_count

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__name

    def get(self, browser, route, date):
        logging.info("Get request for %s airline and %s at %s", self.__name, route, date)

        for retry in range(self.__retry_count):
            try:
                browser.get(self.generate_link(route, date))
                break
            except TimeoutException:
                logging.debug("Timeout for getting url")
        else:
            raise Exception("Can't get link")

    @abc.abstractmethod
    def generate_link(self, route, date):
        logger.error("Call not implemented 'generate_link' method")
        raise NotImplementedError

    @abc.abstractmethod
    def parse(self, browser, route, date, request_dateime):
        logger.error("Call not implemented 'parse' method")
        raise NotImplementedError

    def get_parse(self, browser, route, date):
        self.get(browser, route, date)
        now = pd.datetime.today()
        now = now.replace(microsecond=0)
        return self.parse(browser, route, date, now)
