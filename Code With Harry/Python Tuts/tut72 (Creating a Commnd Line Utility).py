# CREATING A COMMAND LINE UTILITY
import argparse
import sys

def calc(args):
    if args.o == "add":
        return args.X + args.Y

    elif args.o == "mul":
        return args.X * args.Y

    elif args.o == "sub":
        return args.X - args.Y

    elif args.o == "div":
        return args.X / args.Y

    else:
        return "Something went wrong."

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--X', type= float,default=1.0,
                        help="Enter first No.This is a utility for calculating numbers.")

    parser.add_argument('--Y', type=float, default=1.0,
                        help="Enter second No.This is a utility for calculating numbers.")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation.")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
