def pig_latin(name):
    vowels = 'aeiouAEIOU'
    if name[0] in vowels:
        return name + 'yay'
    else:
        return name[1:] + name[0] + 'ay'