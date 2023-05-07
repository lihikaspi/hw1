import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import data
import statistics

def print_stats(subtitle, data, features, path, is_all, which_feature):
    print(subtitle + ":\n")
    statistic_functions = [statistics.calc_mean, statistics.calc_stdv]
    statistic_functions_joint = [statistics.calc_covariance]
    dt = data.load_data(path, features)
    df = data
    if is_all == 0:
        filter = data.filter_by_feature(dt, features[which_feature], {1})
        df = filter[0]
    data.print_details(df, features[2:], statistic_functions)
    data.print_joint_details(df, features[3:], statistic_functions_joint, "cov(t1,cnt)")

def main(argv):
    path = "C:\Users\lihi\OneDrive - Technion\שנה א\מבוא להנדסת נתונים\HW1\london.csv"
    features = ["season", "is_holiday", "hum", "t1", "cnt"]
    print("Question 1:\n")
    print_stats("Summer", data, features, path, 0, 0)
    print_stats("Holiday", data, features, path, 0, 1)
    print_stats("All", data, features, path, 1, -1)

    print("Question 2: \n")
    winter_only = data.filter_by_feature(data, "season", {3})
    holiday = data.filter_by_feature(winter_only, "is_holiday", {0})
    print("If t1<=13.0, then:\n")
    statistics.population_statistics("Winter holiday records", holiday[1], "t1", "cnt", 13.0, 0,
                                     [statistics.calc_mean, statistics.calc_stdv])
    statistics.population_statistics("Winter weekday records", holiday[0], "t1", "cnt", 13.0, 0,
                                     [statistics.calc_mean, statistics.calc_stdv])
    print("If t1>13.0, then:\n")
    statistics.population_statistics("Winter holiday records", holiday[1], "t1", "cnt", 13.0, 1,
                                     [statistics.calc_mean, statistics.calc_stdv])
    statistics.population_statistics("Winter weekday records", holiday[0], "t1", "cnt", 13.0, 1,
                                     [statistics.calc_mean, statistics.calc_stdv])
    # double code --> fix



if __name__ == '__main__':
    main(sys.argv)


