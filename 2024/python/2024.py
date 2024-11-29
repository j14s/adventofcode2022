import argparse
import importlib
import sys

def main(day, part):
  # generate the input file name
  the_days_data="./inputs/" + day + ".input"

  # import the day's module based on the 'day' arguement
  try:
    mod = importlib.import_module("aoc_2024_days." + day)
  except Exception as mod_e:
    print(f"{mod_e}")
    sys.exit(1)

  # build a func call from the above importlib and 'part' arguement
  try:
    ringTheBells = getattr(mod, "p" + part)
  except Exception as attr_e:
    print(f"{attr_e}")
    sys.exit(1)

  # run the appropriate module(day)/part and print results
  results = ringTheBells(the_days_data)
  print(results)

if __name__ == "__main__":
  """ handle the arguements and do the work """
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--day", type=str, help="day(e.g., 2)", required=True)
  parser.add_argument("-p", "--part", type=str, help="part(e.g., 1)", required=True)
  args = parser.parse_args()

  main(args.day, args.part)