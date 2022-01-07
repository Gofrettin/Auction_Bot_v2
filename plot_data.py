import json
import os
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates


def load_item(file, item_name, debug=False):
    item_list = []
    with open(file) as jsonFile:
        json_list = json.load(jsonFile)
        jsonFile.close()
    for element in json_list:
        if debug:
            print("Current item: " + element.get("name"))
        if element.get("name") == item_name:
            item_list.append(element)

    return item_list


def load_specific_items(path, item_name, debug=True):
    item_stack = []
    files = os.listdir(path)

    for filename in files:
        if debug:
            print("Current file: " + filename)
        item_stack.append(load_item(path + filename, item_name))

    return item_stack


def plot_prices(item_stack):
    all_prices = []
    all_dates = []
    for element in item_stack:
        prices = []
        date = []
        date_set = False
        for item in element:
            prices.append(float(item["price per unit"]))
            if date_set == False:
                date.append(datetime.strptime(item["date"], '%Y_%m_%d_%H_%M_%S'))
                date_set = True
        all_prices.append(prices)
        all_dates.append(date)

    all_prices = np.array(all_prices)
    #all_dates = np.array(all_dates, dtype=datetime)
    avg_prices = np.array([])
    max_prices = np.array([]) # ToDo: Implement
    min_prices = np.array([]) # ToDo: Implement

    for i in range(all_prices.shape[0]):
        avg_prices = np.append(avg_prices, np.mean(all_prices[i]))
    plt.plot_date(all_dates, avg_prices, linestyle='solid', marker=',')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return


