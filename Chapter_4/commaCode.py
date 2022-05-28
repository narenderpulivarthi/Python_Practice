spam = ['apples','bananas','tofu','cats']

def listToString(listArg):
    stringList = ''
    for i in range(len(listArg)):
        if i > 0:
            if i == len(listArg) - 1:
                stringList = stringList + ' and '
            else:
                stringList = stringList + ', '
        stringList = stringList + listArg[i]
    return stringList

print(listToString(spam))