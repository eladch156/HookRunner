from argparse import ArgumentParser
from Env.EnvSingleton import Environment


class ArgReader():
    def __init__(self):
        self.__arg_parser = ArgumentParser(description="Hook Runner Service.")
        _mutuall_exclusisve_group = \
            self.__arg_parser.add_mutually_exclusive_group(required=True)
        _mutuall_exclusisve_group.add_argument("-v",
                                               "--version",
                                               help="Show"
                                               " version and exit.",
                                               action='store_true')
        _mutuall_exclusisve_group.add_argument("-c",
                                               "--configuration_file",
                                               help="Configuration file.",
                                               action='store')
        self.__env_singleton = Environment()

    def parse(self):
        args = self.__arg_parser.parse_args()
        if args.version:
            print(self.__env_singleton["version"])
            exit()
        elif args.configuration_file:
            self.__env_singleton["configuration_file"] =\
                args.configuration_file
