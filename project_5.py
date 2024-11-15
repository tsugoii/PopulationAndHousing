"""
Week 5: I/O
"""

import sys
import pandas
import matplotlib.pyplot as plt
MAIN_MENU_QUESTION = ""

def upper_input():
    """Converts input to uppercase"""
    x_x = input()
    return x_x.upper().strip()

def my_quit():
    """This will Quit"""
    print("Thank you for utilizing the Python Data Analysis application!")
    sys.exit()

def validator(x_x):
    """Prompts user to validate their input"""
    valid_input = False
    while valid_input is not True:
        print("Is the following input correct:" , x_x.upper() , "\tYes or No?")
        validator_correctness = input()
        if validator_correctness.upper() == "YES":
            print("Thank you for confirming")
            return True
        if validator_correctness.upper() == "NO":
            print("Understood, reprompting...")
            return False
        if validator_correctness.upper() == "QUIT":
            print("Are you sure you'd like to Quit?")
            quit_check = input()
            if quit_check.upper() == "YES":
                print("Goodbye")
                sys.exit()
            elif quit_check.upper() == "NO":
                print("Returning Back")
                break
            else:
                print("Please Enter 'Yes' or 'No'")
        else:
            print("Please Enter 'Yes' or 'No'")

def population_data():
    """Main Landing For Population"""
    print("You have entered Population Data")
    sub_menu_question = ""
    while sub_menu_question != "EXIT":
        print("Please select the Column you would like to analyze:")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")
        sub_menu_question = upper_input()
        if sub_menu_question == "A":
            validator(sub_menu_question)
            pop_apr()
        elif sub_menu_question == "B":
            validator(sub_menu_question)
            pop_jul()
        elif sub_menu_question == "C":
            validator(sub_menu_question)
            change_pop()
        elif sub_menu_question == "D":
            validator(sub_menu_question)
            break
        else:
            print("***Invalid Input***")
            print("Please Enter 'A' , 'B' , 'C' , or 'D'\t")

def pop_apr():
    """Main Landing For April 1st"""
    print("You have selected the Population From Apr 1st")
    print("The statistics for this column are:")
    df = pandas.read_csv(r"PopChange.csv", usecols=[4])
    table_value = 'Pop Apr 1'
    print_all_the_things(df, table_value)

def pop_jul():
    """Main Landing For July 1st"""
    print("You have selected the Population From July 1st")
    print("The statistics for this column are:")
    df = pandas.read_csv(r"PopChange.csv", usecols=[5])
    table_value = 'Pop Jul 1'
    print_all_the_things(df, table_value)

def change_pop():
    """Main Landing for Population Change"""
    print("You have selected the Population From Population Change")
    print("The statistics for this column are:")
    df = pandas.read_csv(r"PopChange.csv", usecols=[6])
    table_value = 'Change Pop'
    print_all_the_things(df, table_value)

def housing_data():
    """Main Landing for Housing Data"""
    print("You have entered Housing Data")
    sub_menu_question = ""
    while sub_menu_question != "EXIT":
        print("Please select the Column you would like to analyze:")
        print("a. AGE")
        print("b. BEDRMS")
        print("c. BUILT")
        print("d. ROOMS")
        print("e. UTILITY")
        print("f. Quit")
        sub_menu_question = upper_input()
        if sub_menu_question == "A":
            validator(sub_menu_question)
            house_age()
        elif sub_menu_question == "B":
            validator(sub_menu_question)
            house_bedrooms()
        elif sub_menu_question == "C":
            validator(sub_menu_question)
            house_built()
        elif sub_menu_question == "D":
            validator(sub_menu_question)
            house_rooms()
        elif sub_menu_question == "E":
            validator(sub_menu_question)
            house_utility()
        elif sub_menu_question == "F":
            validator(sub_menu_question)
            break
        else:
            print("***Invalid Input***")
            print("Please Enter 'A' , 'B' , 'C' , 'D' , 'E' , or 'F'\t")

def house_age():
    """Main Landing for Housing Age"""
    print("You have selected the House Age")
    print("The statistics for this column are:")
    df = pandas.read_csv(r"Housing.csv", usecols=[0])
    table_value = 'AGE'
    print_all_the_things(df, table_value)

def house_bedrooms():
    """Main Landing for House Bedrooms"""
    print("You have selected the House Bedrooms")
    print("The statistics for this column are:")
    df = pandas.read_csv(r"Housing.csv", usecols=[1])
    table_value = 'BEDRMS'
    print_all_the_things(df, table_value)

def house_built():
    """Main Landing for House Built"""
    print("You have selected the House Built")
    print("The statistics for this column are:")
    df = pandas.read_csv(r"Housing.csv", usecols=[2])
    table_value = 'BUILT'
    print_all_the_things(df, table_value)

def house_rooms():
    """Main Landing for House Rooms"""
    print("You have selected the House Rooms")
    print("The statistics for this column are:")
    df = pandas.read_csv(r"Housing.csv", usecols=[4])
    table_value = 'ROOMS'
    print_all_the_things(df, table_value)

def house_utility():
    """Main Landing for House Utility"""
    print("You have selected the House Rooms")
    print("The statistics for this column are:")
    df = pandas.read_csv(r"Housing.csv", usecols=[6])
    table_value = 'UTILITY'
    print_all_the_things(df, table_value)

def data_count(table):
    """Counts Elements in Column"""
    print("The count is:" , len(table))

def data_mean(table, table_value):
    """Gives Mean of Column"""
    print("The mean is:" , table[table_value].mean())

def data_standard_deviation(table, table_value):
    """Gives Standard Deviation of Column"""
    print("The Standard Deviation is:" , table[table_value].std())

def data_min(table, table_value):
    """Gives Minimum of Column"""
    print("The minimum value is:" , table[table_value].min())

def data_max(table, table_value):
    """Gives Maximum of column"""
    print("The maximum value is:" , table[table_value].max())

def data_histogram(table, table_value):
    """Displays Histogram of Column"""
    print("The Histogram of this column is now displayed")
    plt.hist(table[table_value], color="blue", edgecolor="red", alpha=0.5, rwidth=0.05)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title("A Histogram of Data")
    plt.show()

def print_all_the_things(df, table_value):
    """Prints Everything"""
    data_count(df)
    data_mean(df, table_value)
    data_standard_deviation(df, table_value)
    data_min(df, table_value)
    data_max(df, table_value)
    data_histogram(df, table_value)

print("******************************")
print("Welcome to the Python Data Analysis Application!")

while MAIN_MENU_QUESTION != "QUIT":
    print("Please select the file you'd like to utilize OR Quit: ")
    print("1. Population Data")
    print("2. Housing Data")
    MAIN_MENU_QUESTION = upper_input()
    if MAIN_MENU_QUESTION in ('1', 'POPULATION'):
        validator(MAIN_MENU_QUESTION)
        population_data()
    elif MAIN_MENU_QUESTION in ('2', 'HOUSING'):
        validator(MAIN_MENU_QUESTION)
        housing_data()
    elif MAIN_MENU_QUESTION == "QUIT":
        validator(MAIN_MENU_QUESTION)
        my_quit()
    else:
        print("***Invalid Input***")
        print("Please Enter '1' or 'Population'; '2' or 'Housing'; OR 'Quit'\t")
