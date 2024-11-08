
def regres_real_abs(values, regres):
    dif = []
    for value, reg_val in zip(values, regres):
        dif.append(value-reg_val)
    return dif
    