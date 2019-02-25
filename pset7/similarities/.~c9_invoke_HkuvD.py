from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    linesA = a.split("\n")
    linesB = b.split("\n")
    return listCompare(linesA, linesB)


def sentences(a, b):
    """Return sentences in both a and b"""
    sentsA = sent_tokenize(a)
    sentsB = sent_tokenize(b)
    return listCompare(sentsA, sentsB)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    subA = subExtract(a, n)
    subB = subExtract(b, n)
    return listCompare(subA, subB)


def listCompare(lista, listb):
    result = list()
    for la in lista:
        for lb in listb:
            if la == lb:
                if len(result) != 0:
                    flag = False
                    for res in result:
                        if la == res:
                            flag = True
                        break
                    if flag == False:
                        result.append(la)
                else:
                    result.append(la)
    return result


def subExtract(string, n):
    result = list()
    for i in range(len(string)):
        if i + int(n) > len(string):
            break
        result.append(string[i:i+int(n)])
    return result