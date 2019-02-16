import os
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Browser(object):

    def __init__(self, bin_path=None):
        if bin_path is None:
            path_prefix = os.path.dirname(os.path.abspath(__file__))
            if sys.platform == "linux" or sys.platform == "linux2":  # linux
                path_suffix = os.path.join(os.path.pardir, "bin", "linux")
            elif sys.platform == "darwin":  # MAC OS X
                path_suffix = os.path.join(os.path.pardir, "bin", "osx")
            elif sys.platform == "win32" or sys.platform == "win64":  # Windows
                path_suffix = os.path.join(os.path.pardir, "bin", "windows.exe")
            bin_path = os.path.join(path_prefix, path_suffix)

        self.__bin_path = os.path.abspath(os.path.normpath(bin_path))
        self.__driver = webdriver.Safari()

    def __del__(self):
        self.__driver.close()

    def get(self, url):
        object.__getattribute__(self, "_Browser__driver").get(url)

    def wait(self):
        # TODO: parametrize
        return WebDriverWait(self.__driver, 10)

    def __getattribute__(self, key):
        if key not in dir(Browser) and key not in object.__getattribute__(self, "__dict__"):
            return object.__getattribute__(self, "_Browser__driver").__getattribute__(key)

        return object.__getattribute__(self, key)
