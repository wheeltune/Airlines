import numpy as np


class Description(object):

    def __init__(self):
        self.__properties = {}
        self.__locked = False

    def __setitem__(self, key, value):
        if self.__locked and key not in self.__properties:
            raise Exception("Key `{}` not in Desctiption".format(key))
        self.__properties[key] = value

    def __getitem__(self, key):
        if key not in self.__properties:
            raise Exception("Key `{}` not in Desctiption".format(key))
        return self.__properties[key]

    def mix_with(self, other):
        result = Desctiption()
        result.__properties = self.__properties + other.__properties
        result.lock()
        return result

    def lock(self):
        self.__locked = True

    def as_dict(self):
        return self.__properties


class FlightInfo(Description):

    def __init__(self):
        super(FlightInfo, self).__init__()

        self["Airline"] = np.NaN

        self["Departure city"] = np.NaN
        self["Arrival city"] = np.NaN

        self["Request datetime"] = np.NaN

        self["Number of transfers"] = np.NaN
        self["Departure datetime"] = np.NaN
        self["Arrival datetime"] = np.NaN
        self["Food"] = np.NaN

        super(FlightInfo, self).lock()


class FlightClassInfo(Description):

    def __init__(self):
        super(FlightClassInfo, self).__init__()

        self["Class"] = np.NaN
        self["Baggage size"] = np.NaN
        self["Luggage"] = np.NaN
        self["Return"] = np.NaN
        self["Change"] = np.NaN
        self["Baggage count"] = np.NaN
        self["Place choice"] = np.NaN
        self["Price"] = np.NaN
        self["Remaining places"] = np.NaN

        super(FlightClassInfo, self).lock()
