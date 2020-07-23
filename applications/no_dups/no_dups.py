def no_dups(s):
    if len(s) == 0:
        return ""
    words = s.split(' ')
    uniques = {}
    for word in words:
        if word not in uniques:
            uniques[word] = None
    
    no_dupes = ''
    for key in uniques:
        no_dupes = no_dupes + ' ' + key

    no_dupes = no_dupes[1:]

    return no_dupes


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))