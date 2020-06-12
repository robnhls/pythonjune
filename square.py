
import sys
import argparse

parser = argparse.ArgumentParser(prog="Square Utillity")
parser.add_argument("numbers", nargs="*", type=int,
                    help="The number(s) to be squared")

parser.add_argument(
    "-d", "--debug", help="Prints additional information while executing", action="store_true")

args = parser.parse_args()
# print(args.number ** 2)

if args.debug:
    print(f"Received {len(args.numbers)} parameters")

for number in args.numbers:
    if args.debug:
        print(f"Squaring {number}")
    print(number ** 2)

# python square.py 10
# 100

# python square.py 10 20 30
# 100
# 400
# 900

# for parameter in sys.argv[1:]:
#     number = int(parameter)
#     print(number ** 2)
