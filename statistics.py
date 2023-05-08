from math import sqrt


def calc_mean(values):
    """
    calculate mean value
    :param values: value
    :return: mean value
    """
    n = len(values)
    sum = 0
    for i in range(n):
        sum += values[i]
    return sum/n


def calc_stdv(values):
    """
    calculate standard deviation value
    :param values: value
    :return: stdv value
    """
    n = len(values)
    mean = calc_mean(values)
    sum = 0
    for i in range(n):
        sum += (values[i] - mean) ** 2
    return sqrt(sum/(n-1))


def calc_covariance(values1, values2):
    """
    calculate covariance value
    :param values1: value 1
    :param values2: value 2
    :return: covariance value
    """
    n = len(values1)
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values2)
    sum = 0
    for i in range(n):
        sum += (values1[i] - mean1) * (values2[i] - mean2)
    return sum/(n-1)


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    prints for second question
    :param feature_description: title
    :param data: database
    :param treatment: feature1
    :param target: feature2
    :param threshold: threshold value
    :param is_above: is above threshold
    :param statistic_functions: array of statistic functions
    :return: none
    """
    print(feature_description)
    values_treatment = data[treatment]
    values_target = data[target]
    new_list = []
    if is_above:
        for i in range(len(values_treatment)):
            if values_treatment[i] > threshold:
                new_list.append(values_target[i])
    else:
        for i in range(len(values_treatment)):
            if values_treatment[i] <= threshold:
                new_list.append(values_target[i])

    print(target + ": " + "%.2f" % round(statistic_functions[0](new_list), 2)
          + ", %.2f" % round(statistic_functions[1](new_list), 2))  # print two decimal digits





