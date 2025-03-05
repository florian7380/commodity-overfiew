# calculating a relative difference by dividing the absolut difference with the regression
def regres_real_rel(difference, regres):
    dif_rel = []
    for dif, reg in zip(difference, regres):
        dif_rel.append(dif/reg)
    return dif_rel
    