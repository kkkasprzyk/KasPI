import matplotlib.pyplot as plt

from config_kaspi import *
## Revision of code 27.04.2024 - Release 3 ##  -- > plotter.py module

def plotter(income_traffic, outcome_traffic, typeof_traffic, figure):
    plt.figure(figure)
    plt.clf()  # Wyczyść aktualny wykres przed narysowaniem nowego

    # Upewnij się, że income_traffic i outcome_traffic są listami
    if not isinstance(income_traffic, list):
        income_traffic = [income_traffic]
    if not isinstance(outcome_traffic, list):
        outcome_traffic = [outcome_traffic]

    plt.scatter(range(len(income_traffic)), income_traffic, label='In Counts')
    plt.scatter(range(len(outcome_traffic)), outcome_traffic, label='Out Counts')
    plt.xlabel('Frame')
    plt.ylabel('Count')
    plt.title(typeof_traffic)
    plt.legend()
    plt.pause(0.001)  # Wymuszona aktualizacja wykresu