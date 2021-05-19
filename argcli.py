import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Enter the input")
args = vars(ap.parse_args())

print(args["input"])
