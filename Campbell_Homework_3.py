# -*- coding: utf-8 -*-
"""
Chris Campbell
2/20/19
Python 1 - Dat 119 - Spring 2019
Homework 3

"""

print("Formatting an amount of seconds as the amount of hours, minute and seconds.")

#constants for amount of seconds in a minute and hour
seconds_per_minute = 60
seconds_per_hour = 3600

#ask for an amount of seconds from the user as variable "seconds"
seconds = input("Please enter an amount of seconds: ")

#change seconds variable to an integer
seconds = int(seconds)

#calculate minutes
minutes = (seconds / seconds_per_minute) % (seconds_per_minute)
#set minutes to integer so it displays the amount of whole minutes (17) and not 17.56666666
#divide with "%" and not "/" to use modulo
minutes = int(minutes)

#calculate hours
hours = (seconds / seconds_per_hour)
#set hours to integer so it displays the whole number amount of hours
hours = int(hours)

#calculate seconds remaining after hours and minutes are taken away
seconds_remaining = (seconds - (hours * seconds_per_hour) - (minutes * seconds_per_minute))
seconds_remaining = int(seconds_remaining)

print(hours,"hours,",minutes, "minutes and",seconds_remaining,"seconds")





# print( 5 % 2 ) # modulo - the remainder after integer division
#4,654 Seconds = 1 Hour, 17 Minutes and 33 Seconds 

