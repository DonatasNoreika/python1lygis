def kmi(svoris, ugis):
    if svoris < 30:
        raise ValueError("Svoris per mažas")
    if svoris > 200:
        raise ValueError("Svoris per didelis")
    if ugis < 1.0:
        raise ValueError("Ūgis per mažas")
    if ugis > 3.0:
        raise ValueError("Ūgis per didelis")
    return svoris / (ugis**2)
