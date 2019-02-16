import argparse
import logging

from src import run
from src.utils import *
from src.route import Route


logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("Aeroflot").setLevel(logging.DEBUG)
logging.getLogger("Airline").setLevel(logging.DEBUG)


def main():
    parser = argparse.ArgumentParser(description='Collect airlines flight info')

    parser.add_argument(
        '-r', '--route', action='append', dest='routes',
        help='route in format `MOW-LON`')

    parser.add_argument(
        '-a', '--airline', action='append', dest='airlines',
        help='airlines list [Aeroflot, UralAirlines, Utair]')

    parser.add_argument(
        '-j', '--jobs', type=int, default=4, dest='num_jobs',
        help='number of jobs')

    args = parser.parse_args()

    if args.routes is not None:
        routes = detect_routes(args.routes)
    else:
        routes = default_routes()

    if args.airlines is not None:
        airlines = detect_airlines(args.airlines)
    else:
        airlines = default_airlines()

    run(airlines, routes, args.num_jobs)


if __name__ == "__main__":
    main()