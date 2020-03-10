foregin = ['ą','ę','ż','ź','ć','ń','ś','ł','ó']

def normalize(string):
    wynik = []
    for i in string:
        if i.lower() in foregin:
            continue
        else:
            wynik.append(i)
    return wynik

def ekstratest(extra):
    extra = list(extra)
    if len(extra) < 2:
        return 0
    print(extra)
    if extra[0].isalpha() and extra[1].isalpha():
        return 1
    else:
        return 0

def nwd(a, b):
        if b > 0:
            return nwd(b, a % b)
        else:
            return a

def revmod(a, m):
        a = a % m
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return 1