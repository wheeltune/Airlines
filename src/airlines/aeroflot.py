from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging
import pandas as pd
import re

from ..browser import TimeoutException
from ..descriptions import FlightInfo, FlightClassInfo

from .airline import Airline


__all__ = ["Aeroflot"]


logger = logging.getLogger("Aeroflot")


class Aeroflot(Airline):
    def __init__(self, retry_count=5):
        super(Aeroflot, self).__init__("Аэрофлот", retry_count)

    def get(self, browser, route, date):
        super(Aeroflot, self).get(browser, route, date)

        for retry in range(self.retry_count):
            try:
                browser.wait().until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.button--wide.button--lg')))

                browser.find_element_by_css_selector('.button.button--wide.button--lg').click()
                break
            except TimeoutException:
                pass
        else:
            logger.error("Couldn't load search button")
            raise Exception("Couldn't load search button")

        for retry in range(self.retry_count):
            try:
                browser.wait().until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'js-tariff-helper')))
                break
            except TimeoutException:
                logger.debug("Timeout waiting page preparation")
        else:
            ogger.error("Couldn't load flights table")
            raise Exception("Couldn't load flights table")

    @staticmethod
    def generate_date(date):
        return str(date.year) + str(date.month).zfill(2) + str(date.day).zfill(2)

    def generate_link(self, route, date):
        return "https://www.aeroflot.ru/sb/app/ru-ru#/search"\
               "?adults=1&cabin=econom&children=0&infants=0"\
               "&routes={}.{}.{}-{}.{}.{}".format(
                    route.source.code, self.generate_date(date), route.target.code,
                    route.target.code,   self.generate_date(date), route.source.code)

    def parse(self, browser, route, date, request_dateime):
        result = pd.DataFrame()

        flight_info = FlightInfo()
        flight_info["Airline"] = self.name

        directions = browser.find_elements_by_class_name("js-tariff-helper")
        for i, direction in enumerate(directions[:2]):
            if i == 0:
                flight_info["Departure city"] = route.source.name
                flight_info["Arrival city"]   = route.target.name
            else:
                flight_info["Departure city"] = route.target.name
                flight_info["Arrival city"]   = route.source.name

            for flight in direction.find_elements_by_class_name("flight-search"):
                flight.click()
                # flight_info["Request datetime"] = request_dateime

                # times = flight.find_elements_by_class_name("time-destination__time")
                # flight_info["Number of transfers"] = int(len(times) / 2)

                # times = (times[0], times[-1])
                # times = list(map(lambda element: element.get_attribute("innerHTML"), times))
                # times = list(map(lambda text_time: re.findall("\d+", text_time), times))
                # times = list(map(lambda arr_time: date.replace(hour=int(arr_time[0]), minute=int(arr_time[1]), second=0, microsecond=0), times))

                # flight_info["Departure datetime"] = times[0]
                # if times[1] < times[0]:
                #     times[1] += pd.Timedelta("1 day")
                # flight_info["Arrival datetime"] = times[1]

                # flight_info["Food"] = True

                # flight.click()

                # price_table_rows = browser.find_elements_by_css_selector(".tariff-detail__table .tariff-detail__table-row")

                # classes = list(map(
                #     lambda element: re.sub("[<]\w+[>]", " ", element.get_attribute("innerHTML")).strip(),
                #         price_table_rows[0].find_elements_by_css_selector(
                #             ".tariff-detail__table-cell-wrapper .tariff-detail__table-cell span:first-of-type")))

                # class_infos = [ FlightClassInfo() for i in range(len(classes)) ]
                # for (class_info, flight_class) in zip(class_infos, classes):
                #     class_info["Class"] = flight_class
                #     if re.search("бизнес", flight_class.lower()):
                #         class_info["Baggage size"] = 32
                #         class_info["Luggage"] = 15
                #     else:
                #         class_info["Baggage size"] = 23
                #         class_info["Luggage"] = 10

                # return_infos = price_table_rows[2].find_elements_by_css_selector(".tariff-detail__table-cell")[1:]
                # return_infos = list(map(lambda element: element.get_attribute("innerHTML"), return_infos))

                # change_indos = price_table_rows[3].find_elements_by_css_selector(".tariff-detail__table-cell")[1:]
                # change_indos = list(map(lambda element: element.get_attribute("innerHTML"), change_indos))

                # baggage_count_infos = price_table_rows[4].find_elements_by_css_selector(".tariff-detail__table-cell")[1:]
                # baggage_count_infos = list(map(lambda element: re.sub("[^\d]", "", element.get_attribute("innerHTML")), baggage_count_infos))

                # place_coise_infos = price_table_rows[7].find_elements_by_css_selector(".tariff-detail__table-cell")[1:]
                # place_coise_infos = list(map(lambda element: element.get_attribute("innerHTML"), place_coise_infos))

                # for (class_info, info) in zip(class_infos, zip(return_infos, change_indos, baggage_count_infos, place_coise_infos)):
                #     class_info["Return"] = info[0]
                #     class_info["Change"] = info[1]
                #     class_info["Baggage count"] = info[2]
                #     class_info["Place choice"] = info[3]

                # prices = price_table_rows[1].find_elements_by_css_selector(".tariff-detail__table-price")
                # for (class_info, price_element) in zip(class_infos, prices):
                #     price = price_element.find_element_by_css_selector("span")
                #     price = re.sub("[^\d]", "", re.sub("[<][^>]*[>]", "", price.get_attribute("innerHTML")))
                #     class_info["Price"] = int(price)
                #     try:
                #         places_num = price_element.find_element_by_css_selector("div")
                #         places_num = re.sub("[^\d]", "", places_num.get_attribute("innerHTML"))
                #         class_info["Remaining places"] = places_num
                #     except NoSuchElementException:
                #         class_info["Remaining places"] = np.NaN

                # concat = pd.concat(list(map(
                #     lambda class_info: pd.DataFrame(flight_info.mix_with(class_info).as_dict(), index=[0]),
                #     class_infos)))
                # result = result.append(concat)

                # browser.find_element_by_class_name("modal__close").click()

            # price_table_rows = browser.find_elements_by_css_selector(".tariff-detail__table .tariff-detail__table-row")
        return result
