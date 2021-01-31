# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:49:29 2021

@author: Hubert
"""

import pandas as pd
import matplotlib.pyplot as plt

tab = pd.read_csv("./dax.csv", usecols=['Otwarcie', 'Data'], delimiter=';', header=0)


def select_rows():
    for index, row in tab.iterrows():
        # array = row.split(",")
        selected_rows = (row['Otwarcie'], row['Data'])
    return selected_rows


def draw_plot():
    x = []
    y = []

    for index, line in tab.iterrows():
        x.append(line[0])
        y.append(line[1])

    plt.plot(x, y, label='Dax_price')
    plt.xlabel('Data')
    plt.ylabel('Cena')

    plt.title('Cena Daxa')
    plt.legend()

    plt.show()


print(select_rows())
print(draw_plot())
