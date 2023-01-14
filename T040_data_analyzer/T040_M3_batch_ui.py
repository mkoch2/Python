# Matthew Koch, Carolyn Grum, Beth Pearson

from T040_M1_load_data import add_average as add_avg
from T040_M1_load_data import load_data as ld
from T040_M2_curve_fit import *
from T040_M2_histogram import *
from T040_M2_student_list import *
from T040_M3_maximum import *
from T040_M3_minimum import *


list_of_supported_operators = ['L', 'S', 'H', 'W', 'B', 'Q']
figure_attributes = ['Age', 'StudyTime', 'Failures', 'Health', 'Absences']
more_figure_attributes = ['School', 'G1', 'G2', 'G3', 'G_Avg']

figure1 = "The available commands are: \n 1. L)oad Data \n 2. S)ort Data \n 'School' 'Age' 'StudyTime' 'Failures' 'Health' \n 'Absences' 'G1' 'G2' 'G3' 'G_Avg' \n 3. H)istogram \n 'School' 'Age' 'StudyTime' 'Failures' 'Health' \n 'Absences' \n 4. W)orst ____ for Grades \n 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' \n 5. B)est ___ for Grades \n 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' \n 6. Q)uit"


def get_command():
    """returns the outputs for the commands in the text file 
    """
    print(figure1)
    filelocation = input(
        "Please enter the name of the file where your commands are stored: ")

    operator = filelocation
    infile = open(filelocation, 'r')
    for line in infile:
        items = line.split("")
        command = (items[0])
    if command == 'L':

        dictionary_loaded = False
        filename = items[command + 1]
        key = items[filename + 1]
        if key in figure_attributes or more_figure_attributes:
            dictionary = add_avg(ld(filename, key))
            print("Data Loaded")
            print("Data sorted")
            dictionary_loaded = True

        else:
            print("Invalid key.")
            key = input("Please enter a new key:")

    elif command == 'S' and (dictionary_loaded == True):
        attribute = items[command + 1]
        sort = sort_students_bubble(dictionary, attribute)
        prompt = items[attribute + 1]
        if prompt.upper == 'Y':
            print(sort)

    elif command == "H" and dictionary_loaded:
        attribute = items[command + 1]
        hist = histogram(dictionary, attribute)
        prompt = items[attribute + 1]
        if prompt.upper() == 'Y':
            print(hist)

    elif command == "W" and dictionary_loaded:
        attribute = items[command + 1]
        p = minimum(dictionary, attribute)
        print("The worst value for the attribute " +
              attribute + "is" + str(p[0]))

    elif command == "B" and dictionary_loaded:
        attribute = items[command + 1]
        p = maximum(dictionary, attribute)
        print("The best value for the attribute " +
              attribute + "is" + str(p[0]))

    elif command == "Q" and dictionary_loaded:
        print("Program ended")

    else:
        print("File not loaded. Please, load a file first.")









