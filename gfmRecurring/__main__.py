import argparse
import sys

from gfmRecurring.GfmDao import GfmDao
from gfmRecurring.ProcessCommands import ProcessCommands


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?',
                        type=argparse.FileType('r'), default=sys.stdin,
                        help="input file with commands")
    args = parser.parse_args()
    command_lines = args.file.readlines()
    gfm_dao = GfmDao()
    process_commands = ProcessCommands(gfm_dao)
    process_commands.parse_and_process_commands(command_lines)
    process_commands.print_stats()


if __name__ == '__main__':
    main()
