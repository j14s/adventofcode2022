from utils.tools import inputIngest
"""
Skeleton AoC day module with examples
just copy to a new day(<num>.py)
"""


# used by valiadateData()
the_days_data = None

def validateData(the_days_data):
  """ make sure we got data passed in """
  if the_days_data is None:
    raise ValueError('You do not seem to have passed in the_days_data before using this function')

def lineCounter(l_var):
  """ sample func to count lines in the data """
  l_count = 0
  for line in l_var:
    if line != "\n":
      l_count += 1
  return(l_count)

def charCounter(c_var):
  """ sample func to count chars in the data """
  c_count = 0
  for line in c_var:
    if line != "\n":
      c_count += len(line)
  return(c_count)

def daCommon(the_days_data):
  """ function where we put all the processing common to the day's challenge """
  validateData(the_days_data)
  myInput = inputIngest(the_days_data)
  genProc = myInput
  return(genProc)

def p1(the_days_data):
  """ Actual day N's part 1 func to get it's answer """
  # call the general worker func
  general_results = daCommon(the_days_data)

  # do this part's custom stuff
  custom_results = lineCounter(general_results)
  return(custom_results)

def p2(the_days_data):
  """ actual day N's part 1 func to get it's answer """
  # call the general worker func
  general_results = daCommon(the_days_data)

  # do this part's custom stuff
  custom_results = charCounter(general_results)
  return(custom_results)
