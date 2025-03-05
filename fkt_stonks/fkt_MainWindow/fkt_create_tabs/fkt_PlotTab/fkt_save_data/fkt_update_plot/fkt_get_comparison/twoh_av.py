
# Berechnung des 200 day averags
def twoh_av(dates, values):
    length = len(dates)
    av = []
    x = 0.0
    # berechnung der Summe der letzten 200 Tage
    for i in range(136):
        x += values[i]
    # Speichern des ersten Wertes für die Rückgabe
    av.append(x)
    # Abzug des jüngsten und Addition des nächsten Tages
    for i in range(length-136):
        x -= values[i]
        x += values[i+136]
        # Speichern der Werte für die Rückgabe
        av.append(x)
    for i, value in enumerate(av):
        av[i] = value/136
    return av