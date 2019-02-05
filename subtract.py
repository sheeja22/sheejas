# Read inputs from the user.
time1 = int(input("Please enter the first time: "))
time2 = int(input("Please enter the second time: "))

# The following if statement handles the part of the work needed for the
# extra credit portion of this question.
if time2 < time1 :
  time2 = time2 + 2360# Compute the hours and minutes in the difference.
difference = time2 - time1
hours = difference // 100
minutes = difference % 100
