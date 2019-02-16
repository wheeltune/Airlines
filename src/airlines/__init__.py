from .aeroflot import *


AIRLINES = {
    "aeroflot": Aeroflot(),
    # "Utair": Utair(),
    # "UralAirlines": UralAirlines()
}


def airline_factory(airline_name):
    return AIRLINES[airline_name.lower()]
