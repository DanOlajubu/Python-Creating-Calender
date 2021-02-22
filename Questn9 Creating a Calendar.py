#In Python, we can display the calendar of any month of any year by importing the calendar module.


# First import the calendar module
import calendar

# ask of year and month
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy,mm))  
