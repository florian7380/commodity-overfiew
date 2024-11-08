
def regres_real_rel(values, regres):
    dif = []
    for value, reg in zip(values, regres):
        dif.append(value/reg)
    return dif
    