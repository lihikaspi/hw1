import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# season, is_holiday, hum, t1, cnt
def load_data(path, features):
    df = pd.read_csv(path)
    data = df.to_dict(orient = "list")
    for key in data.keys():
        if key not in features:
            data.pop(key)
    return data

# feature = season or is_holiday
def filter_by_feature(data, feature, values):
    data1 = []
    data2 = []
    val = data[feature]
    for i in range(len(val)):
        if val[i] in values:
            data1.append(val[i]) # wrong --> will go back
        elif val[i] not in values:
            data2.append(val[i])
    return data1, data2

# season, is_holiday, hum, t1, cnt
def print_details(data, features, statistic_functions):
    for ft in features:
        print(ft + ":")
        for func in statistic_functions:
            print(func(data[ft]) + ",") # help func to remove comma
        print("\n")

# 2 features
def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    print(statistic_functions_names + ":\n")
    for func in statistic_functions:
        print(func(data[features[0]], data[features[1]]))
