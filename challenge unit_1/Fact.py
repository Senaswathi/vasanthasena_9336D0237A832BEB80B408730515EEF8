def leapyear(year):
  if(year%4==0 and year%100!=0):
    return True
  elif(year%400==0):
    return True
  else:
    return False
year=int(input("enter a year:"))
if leapyear(year):
  print(year,"is a leapyear")
else:
  print(year,"is not a leapyear")