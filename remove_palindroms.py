def remove_palindroms(spells):
    result = []
    for word in spells:
        temp = word.lower().strip()
        if temp != temp[::-1]:
            result.append(word)
    return result
