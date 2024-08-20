import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

run = True

original_df = pd.read_csv('data/games-features.csv')

updated_df = original_df.loc[:,['index', 'QueryID', 'ResponseID', 'QueryName', 'ResponseName', 'ReleaseDate', 'ControllerSupport', 'PlatformWindows', 'PlatformLinux', 'PlatformMac', ]]
updated_df.to_csv('data/games-simple.csv')

def showOG():
    print(original_df)

def showUpdatedDf():
    print(updated_df)

def macGames():
    print("HANG IN THERE, WE'LL BE THERE SOON")

def options():
    print("""   [1] -> View the original dataframe
        [2] -> View the dataframe with only the necessary information
        [3] -> View the most popular macOS games
        [4] -> View the most popular Windows games
        [5] -> View the most popular Linux games
        [6] -> View the games with controller support""")
    print(" ")

while run:
    try:
        options()
        selection = int(input("PLEASE SELECT AN OPTION: "))

        if selection == 1:
            showOG()
        elif selection == 2:
            showUpdatedDf()
        elif selection == 3:
            macGames()

    except ValueError:
        print("BRO ARE YOU STUPID HOW HARD IS IT TO ENTER A NUMBER?!?!?!?!?")
