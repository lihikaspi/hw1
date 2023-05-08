import pandas as pd


# season, is_holiday, hum, t1, cnt
def load_data(path, features):
    """
    load data from path
    :param path: file directory
    :param features: relevant features
    :return: relevant data
    """
    df = pd.read_csv(path)
    data = df.to_dict(orient="list")
    for key in list(data.keys()):
        if key not in features:
            data.pop(key)  # remove irrelevant keys
    return data


def copy(data):
    """
    copy dictionary
    :param data: dict
    :return: copied dict
    """
    new_dict = {}
    for key, value in data.items():
        new_dict[key] = list(value)  # copy value as a new list
    return new_dict


# feature = season or is_holiday
def filter_by_feature(data, feature, values):
    """
    remove unwanted items from database
    :param data: data
    :param feature: to filter by
    :param values: values of feature wanted
    :return: two dictionaries
    """
    data1 = copy(data)
    data2 = copy(data)
    val = data[feature]
    for i in range(len(val)-1, -1, -1):  # loop going backwards
        if val[i] not in values:
            for key in list(data.keys()):
                data1[key].pop(i)  # remove unwanted items
        elif val[i] in values:
            for key in list(data.keys()):
                data2[key].pop(i)  # remove unwanted items
    return data1, data2


# season, is_holiday, hum, t1, cnt
def print_details(data, features, statistic_functions):
    """
    print one value statistic functions
    :param data: database
    :param features: value for statistic functions
    :param statistic_functions: array of functions
    :return: none
    """
    for ft in features:
        values = data[ft]
        print(ft + ": " + "%.2f" % round(statistic_functions[0](values), 2) + ", "
              + "%.2f" % round(statistic_functions[1](values), 2))  # print two decimal digits


# 2 features
def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    """
    print two value statistic functions
    :param data: database
    :param features: value for statistic functions
    :param statistic_functions: array of functions
    :param statistic_functions_names: title to print
    :return:
    """
    print(statistic_functions_names + ": " +
          "%.2f" % round(statistic_functions[0](data[features[0]], data[features[1]]), 2))  # print two decimal digits
