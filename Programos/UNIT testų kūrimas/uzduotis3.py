def kmi(svoris, ugis):
    if svoris <= 20 or svoris >= 240:
        raise ValueError
    if ugis <= 0.40 or ugis >= 3.40:
        raise ValueError
    return round(svoris / ugis ** 2, 1)
