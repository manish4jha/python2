import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("arg1")
parser.add_argument("arg1", help="Give a scalar value")
args = parser.parse_args()
print (args.arg1)
