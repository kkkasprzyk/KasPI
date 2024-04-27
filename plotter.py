import matplotlib.pyplot as plt

from config_kaspi import *
## Revision of code 27.04.2024 - Release 3 ##  -- > plotter.py module
def plotter(income_traffic, outcome_traffic, typeof_traffic, figure_int):

    print ("########### INITIALIZE OF module plotter() ##########")
    plt.scatter(["in countss.."],income_traffic, label='In Counts')
    plt.scatter(["out countss.."],outcome_traffic, label='Out Counts')
    plt.xlabel('Frame')
    plt.ylabel('Count')
    plt.title(typeof_traffic)
    plt.legend()
    plt.draw()
    plt.pause(0.01)  # Pozwól wykresowi zaktualizować się
    plt.clf()  # Wyczyść aktualny wykres, aby narysować nowy