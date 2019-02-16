from .airlines import airline_factory
from .route import Route


__all__ = ["detect_routes", "detect_airlines", "default_routes", "default_airlines"]


def detect_routes(route_codes):
    return list(map(lambda route: Route.from_codes(route), route_codes))


def detect_airlines(airline_names):
    return list(map(lambda airline_name: airline_factory(airline_name), airline_names))


def default_routes():
    route_codes = [
        "MOW-LED", "MOW-LON", "MOW-SVX",
        "MOW-CEK", "MOW-AER", "MOW-BCN",
        "MOW-NCE"
    ]
    return detect_routes(route_codes)


def default_airlines():
    airlines_names = ["Aeroflot"]  #, "Utair", "UralAirlines"]
    return detect_airlines(airlines_names)