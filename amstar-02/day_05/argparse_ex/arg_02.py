import argparse
parser = argparse.ArgumentParser()
'''
The option is now more of a flag than something that requires a value.
We even changed the name of the option to match that idea.
Note that we now specify a new keyword, action,
and give it the value "store_true". This means that, if the option is specified,
assign the value True to args.verbose. Not specifying it implies False.
'''
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print ("the square of {} equals {}".format(args.square, answer))
else:
    print (answer)
