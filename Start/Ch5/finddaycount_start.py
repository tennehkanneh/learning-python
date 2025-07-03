# This is how your code will be called.
# You can edit this code to try different testing cases.
testyear = 2025
testmonth = 12
testday = 0

import calendar

def count_days(year, month, whichday):
  count = 0

  cal = calendar.monthcalendar(year, month)
  print(cal)
    

  for week in cal:
    if week[whichday] != 0:
      count += 1
      print(week[whichday])

  print(f"{whichday} occurs: {count} in {month} of {year}")
  return count



count_days(testyear, testmonth, testday)