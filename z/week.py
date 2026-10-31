def alarm_clock(day, vacation):
  if 1 <= day <= 5 and vacation == False:
    return "7:00"
  elif day == 0 or day == 6 and vacation == False:
    return "10:00"
  elif 0 <= day <= 6 and vacation == True:
    return "10:00"
  elif day == 0 or day == 7 and vacation == True:
    return "off"



print(alarm_clock(0,True))