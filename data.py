import pandas as pd

# season, is_holiday, hum, t1, cnt
def load_data(path, features):
    df = pd.read_csv(path)
    data = df.to_dict(orient="list")
    for key in list(data.keys()):
        if key not in features:
            data.pop(key)
    return data

def copy(data):
    new_dict = {}
    for key, value in data.items():
        new_dict[key] = list(value)
    return new_dict

# feature = season or is_holiday
def filter_by_feature(data, feature, values):
    data1 = copy(data)
    data2 = copy(data)
    val = data[feature]
    for i in range(len(val)-1, -1, -1):
        if val[i] not in values:
            for key in list(data.keys()):
                data1[key].pop(i)
        elif val[i] in values:
            for key in list(data.keys()):
                data2[key].pop(i)
    return data1, data2

# season, is_holiday, hum, t1, cnt
def print_details(data, features, statistic_functions):
    for ft in features:
        values = data[ft]
        print(ft + ": " + "%.2f" % round(statistic_functions[0](values), 2) + ", "
              + "%.2f" % round(statistic_functions[1](values), 2))
        #for func in statistic_functions:
        #    print(func(data[ft]) + ",")  # help func to remove comma

# 2 features
def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    print(statistic_functions_names + ": " +
          "%.2f" % round(statistic_functions[0](data[features[0]], data[features[1]]), 2))