from argparse import ArgumentParser
from Env.EnvSingleton import Environment

class ArgReader():
    def __init__(self):
        self._argParser = ArgumentParser(description="Hook Runner Service.")
        eitherMustGroup = self._argParser.add_mutually_exclusive_group(required=True)
        eitherMustGroup.add_argument("-v","--version",help="Show version and exit.",action='store_true')
        eitherMustGroup.add_argument("-c","--configuration_file",help="Configuration file.",action='store')
        self._envSingleton = Environment()
    def parse(self):
        args = self._argParser.parse_args()
        if args.version:
            print(self._envSingleton["version"])
            exit()
        elif args.configuration_file:
            self._envSingleton["configuration_file"] = args.configuration_file
        
