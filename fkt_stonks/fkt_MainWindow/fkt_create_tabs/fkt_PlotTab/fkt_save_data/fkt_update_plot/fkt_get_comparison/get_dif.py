def get_dif(values):
    return_values = []
    for val1, val2 in zip(values[0], values[1]):
        return_values.append(val1-val2)
    return return_values