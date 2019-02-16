import queue
import threading
from multiprocessing import Pool
import random
import time
import pandas as pd
import logging

from .browser import Browser


def initializer():
    global browser
    print("Starting new")
    browser = Browser()


def parse_task(airline, route, date):
    try:
        global browser
        return airline.get_parse(browser, route, date)
    except Exception as error:
        logging.exception("Catched exception from browser process")


def run(airlines, routes, browsers_count):
    task_args = []
    for date in pd.date_range(pd.datetime.today() + pd.Timedelta("1 day"), periods=12, freq='5D'):
        task_args.extend([ (airline, route, date) for airline in airlines for route in routes ])

    with Pool(processes=browsers_count, initializer=initializer) as pool:
        result_parts = pool.starmap(parse_task, task_args)

    result = pd.DataFrame()
    for part in result_parts:
        result.append(part, ignore_index=True)

    return result
