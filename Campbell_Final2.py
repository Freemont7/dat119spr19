# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:07:24 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Chris Campbell
5/1/19
Python 1 - Dat 119 - Spring 2019
Final Project
"""
    
#open the file containing the usgs data
usgsedit = open('usgsedit.txt', 'r')

#read usgs data from file as 
usgs_data = usgsedit.read()

#close file
usgsedit.close()

#split usgs data string
usgs_data_list=usgs_data.split()

print("Stream conditions for Pine Creek at Waterville, PA from")
print("April 1st through June 30th 2018 (roughly the spring trout season)\n")

while True:




    #ask user for a day
    print("The data range is from 4/1/2018 to 6/30/2018.")
    user_day = input("Please enter a day wthin the range in the format 1/1/2018: \n")
    
    #if user enters a zero before the day (such as 4/01/2018) the program will
    #not find it in the data since date/time is given as 4/1/2018
    if user_day[2] == "0":
    #if user has entered a zero before the day, rebuild string without that zero
        user_day = user_day[:2] + user_day[3:]
        
    #input validation    
    while True:
        
        if user_day not in usgs_data_list:
            print("Day not found.")
            user_day = input("Please enter another day from 4/1/2018 to 6/30/2018: \n")
            if user_day[2] == "0":
                user_day = user_day[:2] + user_day[3:]
        else:
            break
    
    #search data list for first instance of data line containing the user's input day
    index = usgs_data_list.index(user_day)
    #there are 480 lines of data per day
    period = index + 479
    #create day by starting list at first line containing user's day and extending
    #it through last line containing data from user's day
    day = usgs_data_list[index:period]
    
    #ask for a time
    print("Time must be in fifteen minute increments in the format 12:00")
    user_time = input("PLease enter a time: ")
    
    #user_time must be in format 12:00:00 but asking the user for a time 
    #ending in "00" seconds is awkward so this is removed by adding
    #colon and two zeroes to the user's time input
    if len(user_time) <= 6:
        user_time = user_time + ":00"
    
    #input validation   
    while True:
        
        if user_time not in day:
            print("Invalid time.")
            user_time = input("Please enter another time in the format 12:00: ")
            if len(user_time) <= 6:
                user_time = user_time + ":00"
        else:
            break
    
    
            
    
    
    time = day.index(user_time)
    
    #must ask if user wants AM or PM
    am_pm = input("AM or PM?: ")
    
    #input validation
    while True:
        if am_pm == "AM" or am_pm == "PM":
            print("")
            break
        else:
            am_pm = input("Please specify AM or PM: ")
    
    #if pm, add 240 lines to the time value so that the index checked will be
    #for the PM time instead of AM of any time given
    if am_pm == "PM":
        time = time + 240
    
        
    #water data is 2 further in list than the time
    water = time + 2
    #temperature data is 3 spaces in the list away from time data
    temp = time + 3
    #put user's indicated date and time together as a string
    date_time = index + time
    
    #put in water variable as index of list day to get the water
    #data from that specific time on that specific day
    print("The water height was",day[water], "feet.")
    #same for temperature
    print("The water temperature was",day[temp], "degrees fahrenheit.")
    water_float = day[water]
    #water_float = float(water_int)
    
    #function to take in water height value at user's date/time
    #and determine wether the creek was high, low or normal
    def water_height(index):
        value = index
        value = float(value)
        if value >= 3.5:
            print("The water level is too high to fish.")
        elif value <= 2.5:
            print("The water level is low.")
        else:
            print("The water is normal height.")
    
    #function to take in temperature data at user's date/time
    #to determine high, low or ideal
    def water_temp(index):
        value = index
        value = float(value)
        if value >= 68.0:
            print("The water temperature is too high to fish.")
        elif value <= 50.0:
            print("The water temperature is low.")
        else:
            print("The water temperature is ideal.")
    
    #function that looks at temperature data from two times just before
    #user's date/time and compares them to see if temperature was rising or falling
    def temp_trend(index):
        value1 = usgs_data_list[index - 2]
        value2 = usgs_data_list[index - 22]
        if value1 == value2:
            print("The water temperature is stable.")
        if value1 > value2:
            print("The water temperature is rising.")
        if value2 > value1:
            print("The water temperature is falling.")
      
    #looks at water data jsut before user's date/time to see if water
    #was rising or falling
    def water_trend(index):
        value1 = usgs_data_list[index - 3]
        value2 = usgs_data_list[index - 23]
        if value1 == value2:
            print("The water level is stable.")
        if value1 > value2:
            print("The water level is rising.")
        if value2 > value1:
            print("The water level is falling.")
    
    #run the usgs data for user's date/time through the functions to
    #print results
    water_height(day[water])
    water_trend(date_time)
    water_temp(day[temp])
    temp_trend(date_time) 
    
    yes_no = input("would you like check another day/time? yes or no: ")
    while True:
        if yes_no == "yes" or yes_no == "no":
            print("")
            break
        else:
            yes_no = input("Please answer yes or no: ")
    if yes_no == "no":
        print("Thank you. Program closing.")
        break
    else:
        continue


