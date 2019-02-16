CITY_CODES = {
    "Москва": "MOW",
    "Санкт Петербург": "LED",
    "Лондон": "LON",
    "Екатеринбург": "SVX",
    "Челябинск": "CEK",
    "Сочи": "AER",
    "Барселона": "BCN",
    "Ницца": "NCE",
}

CITY_NAMES = { value: key for key, value in CITY_CODES.items() }


class Destination:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    @classmethod
    def from_name(cls, name):
        return cls(name, CITY_CODES[name])

    @classmethod
    def from_code(cls, code):
        return cls(CITY_NAMES[code], code)

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    def __repr__(self):
        return "{} ({})".format(self.__name, self.__code)


class Route:
    def __init__(self, source, target):
        self.__source = source
        self.__target = target

    @classmethod
    def from_codes(cls, codes):
        codes = codes.split('-')
        assert len(codes) == 2
        return cls(
            Destination.from_code(codes[0]),
            Destination.from_code(codes[1])
        )

    @property
    def source(self):
        return self.__source

    @property
    def target(self):
        return self.__target

    def __repr__(self):
        return "{} - {}".format(self.__source, self.__target)
