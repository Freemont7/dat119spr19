# -*- coding: utf-8 -*-
"""
Chris Campbell
3/27/19
Python 1 - Dat 119 - Spring 2019
Week 8
"We’re going to create an application to track a user’s todo list!

Our application will maintain at least two lists: 
1)	items that need to be done and 
2)	items that have already been completed."

"""
#create todo list and completed tasks list with nothing in them
todo_list = ["run", "eat", "breathe"]
completed_tasks = []

#greeting
print("Welcome to the ToDo list tracker: ")
print("")

#main function to run loop
def main():
    
    #while loop to make sure user selects an item (1-5) from the menu
    #if not, ask again
    choice = 0
    while choice != 5:
        main_menu()
        choice = input("Enter your choice: ")
        print("")
        
        #if elif statements to correspond user's choice to running the
        #function that relates to that choice
        #IE if they choose 1, then run function to display todo list
        if choice == "1":
            display_todo_list()
        elif choice == "2":
            display_completed_list()
        elif choice == "3":
            add_item_todo_list()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Thank you. Program exitting.")
            break
        else:
           print("Invalid selection. Please choose a choice between 1 and 5: ")
           print("")


#function to define menu
def main_menu():
    print(" Menu ")
    print("1 View ToDo list")
    print("2 View completed tasks")
    print("3 Add item to ToDo list")
    print("4 Mark item as completed")
    print("5 Exit")

#function to display todo list
def display_todo_list():
    
    for object in todo_list:
        #print list as numbered list of items
        print(todo_list.index(object) +1, object)

    #if todo list is empty, do not proceed and give this message and return to menu
    if todo_list == []:
        print("There is nothing on the ToDo list.")
    print("")

#completed list function
def display_completed_list():

    for object in completed_tasks:
        print(completed_tasks.index(object) +1, object)
    
    if completed_tasks == []:
        print("There are no completed items.")
    print("")


#function to add item to todo list
def add_item_todo_list():
    additem = input("Type in a task to add to ToDo list: ")
    todo_list.append(additem)


#function to add item to completed list and remove from todo list
def mark_completed():
    display_todo_list()
    #do not proceed if todo list is empty
    if todo_list == []:
        print("There is nothing to mark as completed. ")
        print("")
        #main_menu()
    #if todo has an item, then:
    if todo_list != []:
        #while loop and then if else statements to check that input
        #is first a number and second not greater than the amount of items
        #which are on the todo list
        while True:
            #get length of todo list
            length = len(todo_list)
            completed = input("Select number of item to mark as completed: ")
            try:
                #make sure user input is an integer
                val = int(completed)
                completed = int(completed)
                #if user input is not a number on the list, print error
                #and ask again
                if completed > length:
                    print("Invalid, number is not on list")
                if completed <= 0:
                    print("Choose a number greater than 0")
                else:
                    completed_value = todo_list[completed-1]
                    todo_list.remove(completed_value)
                    completed_tasks.append(completed_value)
                    print("")
                    break
            #if not an integer, give this error and ask for another input
            except ValueError:
                print("Input invalid. Please select a number corresponding to an item on the list")
        #if completed != 1 to len(todo_list):
        #completed = input("Please select the number of an item on the todo list: ")
            
#run main
main()