
def compare_shares(values, calc_values):
    comp = 0.0
    for val, cal in zip(values, calc_values):
        comp += abs(val-cal)
    comp /= len(values)
    
    return comp