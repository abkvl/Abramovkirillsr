def remove_palindroms(spells):
    for j in spells:
        a = j.lower()
        if a == a[::-1]:
            spells.remove(a)
    return spells
