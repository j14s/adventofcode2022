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
  first = []
  second = []
  for pair in inputIngest(the_days_data):
    res1, res2 = pair.split()
    first.append(res1)
    second.append(res2)
  first.sort()
  second.sort()
  return(first, second)

def p1(the_days_data):
  """ Actual day N's part 1 func to get it's answer """
  # call the general worker func
  first, second = daCommon(the_days_data)
  count = len(second)
  step = 0
  tot_dist = 0
  while step < count :
    firint = int(first[step])
    secint = int(second[step])
    if firint != secint:
      if firint > secint:
        tot_dist += firint - secint
      else:
        tot_dist += secint - firint
    step += 1
  # do this part's custom stuff

  return(f"The distance is: {tot_dist}")

def p2(the_days_data):
  """ actual day N's part 1 func to get it's answer """
  # call the general worker func
  first, second = daCommon(the_days_data)
  count = len(first)
  step = 0
  tot_dist_mod = 0
  while step < count :
    firstr = first[step]
    if firstr in second:
      el_count = second.count(firstr)
      dist_mod = int(firstr) * el_count
      tot_dist_mod += dist_mod
    step += 1

  # do this part's custom stuff
  return(f"Weighted total distance: {tot_dist_mod}")
