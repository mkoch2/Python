# Matthew Koch, Carolyn Grum, Beth Pearson


import numpy as np
import matplotlib.pyplot as plt
from T040_M1_load_data import load_data
from T040_M1_load_data import add_average as add_avg
from T040_M2_sort_plot import student_list as sl
from T040_M2_curve_fit import curve_fit as cf
from scipy.optimize import fminbound
from T040_M2_sort_plot import histogram
from T040_M2_sort_plot import sort_students_selection
from T040_M3_minimum import curve_function
from T040_M3_minimum import minimum
from T040_M3_maximum import maximum

# C:\Users\cgdoo\Pictures\Code\student-mat.csv

main_dictionary = {}

user_interface = ("1. L)oad Data \n2. S)ort Data \n    'School'    'Age'   'StudyTime'    'Failures'    'Health'\n    'Absences'    'G1'    'G2'    'G3'    'G_Avg'\n3. H)istogram \n    'School'    'Age'    'StudyTime'    'Failures'    'Health'\n    'Absences'\n4. W)orst ____ for Grades\n    'Age'    'StudyTime'    'Failures'    'Health'    'Absences'\n5. B)est ____ for Grades\n    'Age'    'StudyTime'    'Failures'    'Health'    'Absences'\n6. Q)uit")

print(user_interface)
command = input("Please type your command: ")

while len(command) >= 1:
    if command == "l" or command == 'L':  # calls for load data
        # sends out filename
        file_name = input("please enter the name of the file: ")
        # asks attribute
        attribute = input("please enter the attribute to use as key: ")
        # check and good
        # this is the dictionary
        main_dictionary = add_avg(load_data(file_name, attribute))
        print("Data Loaded")
        print(user_interface)
        command = input("Please type your command: ")

    elif command == "S" or command == 's':  # calls to sort data
        if main_dictionary != {}:  # If data is loaded
            # find attribute to sort
            attribute = input(
                "please enter the attribute you want to use for sorting: \n'School'    'Age'   'StudyTime'    'Failures'    'Health'    'Absences'\n    'G1'    'G2'    'G3'    'G_Avg': ")
            print1 = input(
                "Data Sorted. Do you want to display the data? Y/N: ")
            if print1 == 'Y' or print1 == 'y':  # does someone want it to print
                # prints sorted data
                print(sort_students_selection(main_dictionary, attribute))
                print(user_interface)
                command = input("Please type your command: ")

            elif print1 == 'N' or print1 == 'n':  # does not print sorted data
                print(user_interface)
                command = input("Please type your command: ")

            else:
                print("Invalid command")  # not a valid input
                print(user_interface)
                command = input("Please type your command: ")

        else:
            print("please load data")  # no data loaded yet
            print(user_interface)
            command = input("Please type your command: ")

    elif command == "H" or command == 'h':  # for histogram
        if main_dictionary != {}:  # check data loaded
            # attribute to find data
            attribute = input(
                "Please enter an attribute you want to use for sorting:\n'School'    'Age'   'StudyTime'    'Failures'    'Health'\n    'Absences':  ")
            # do you want to print histogram
            print1 = input("do you want to display the data? Y/N: ")
            if print1 == 'Y' or print1 == 'y':
                # create histogram
                print("Data Loaded")
                print(histogram(main_dictionary, attribute))
                command = input("Please type your command: ")

            elif print1 == 'N' or print1 == 'n':  # does not print sorted data
                print(user_interface)
                command = input("Please type your command: ")

            else:
                print("Invalid command")  # invalid input
                print(user_interface)
                command = input("Please type your command: ")

        else:
            print("Please load data")  # no data loaded yet
            print(user_interface)
            command = input("Please type your command: ")

    elif command == "W" or command == 'w':  # Find worst G_Avg for attribute
        if main_dictionary != {}:  # If data is loaded
            # find attribute to sort
            attribute = input(
                "please enter the attribute you want to calculate worst value of the attribute for in terms of grades: \n'Age'   'StudyTime'    'Failures'    'Health'    'Absences': ")
            print1 = input(
                "Data Sorted. Do you want to display the data? Y/N: ")
            if print1 == 'Y' or print1 == 'y':  # does someone want it to print
                # prints sorted data
                print("the worst value for the attribute is:",
                      minimum(attribute))
                print(user_interface)
                command = input("Please type your command: ")

            elif print1 == 'N' or print1 == 'n':  # does not print sorted data
                print(user_interface)
                command = input("Please type your command: ")

            else:  # invalid input
                print("Invalid command")
                print(user_interface)
                command = input("Please type your command: ")

        else:
            print("please load data")  # no data loaded yet
            print(user_interface)
            command = input("Please type your command: ")

    if command == "B" or command == 'b':  # sort data for best G_Avg
        if main_dictionary != {}:  # If data is loaded
            # find attribute to sort
            attribute = input(
                "please enter the attribute you want to calculate the best value of in terms of grades: \n'Age'   'StudyTime'    'Failures'    'Health'    'Absences': ")
            print1 = input(
                "Data Sorted. Do you want to display the data? Y/N: ")
            if print1 == 'Y' or print1 == 'y':  # does someone want it to print
                # prints sorted data
                list1 = (sort_students_selection(main_dictionary, 'G_Avg'))
                print("the best value for the attribute is:",
                      maximum(attribute))  # From best G_Avg
                print(user_interface)
                command = input("Please type your command: ")

            elif print1 == 'N' or print1 == 'n':  # does not print sorted data
                print(user_interface)
                command = input("Please type your command: ")

            else:
                print("Invalid command")  # invalid input
                print(user_interface)
                command = input("Please type your command: ")

        else:
            print("please load data")  # no data loaded yet
            print(user_interface)
            command = input("Please type your command: ")

    elif command == "Q" or command == 'q':  # ends cycle
        print("Quitting")
        break

    else:
        print("Invalid Command")
        print(user_interface)
        command = input("Please type your command: ")
