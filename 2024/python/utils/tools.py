from os import read
import sys

def inputIngest(in_file):
  """
  Open the input file and return it
  split by line....or throw an exception
  """
  try:
    with open(in_file) as file:
      return(file.read().splitlines())
  except Exception as open_err:
    print(f"{open_err}")
    sys.exit(1)