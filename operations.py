alphabetdict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
result = []
alphabetdictreverse = {v: k for k, v in alphabetdict.items()}

from utility import *

def decrypt(key,crypto):
    for i in crypto:
        flag = 0
        if i.isalpha():
            if i.isupper():
                flag = 1
            add = (alphabetdict[i.lower()] - int(key)) % 26
            if flag == 1:
                result.append(alphabetdictreverse[add].upper())
            elif flag == 0:
                result.append(alphabetdictreverse[add])
        else:
            result.append(i)
    return result


def decryptaffi(crypto,a,b):
    x=1
    x = revmod(a,26)
    for i in crypto:
        flag = 0
        if i.isalpha():
            if i.isupper():
                flag = 1
            add = x * (alphabetdict[i.lower()] - b) % 26
            if flag == 1:
                result.append(alphabetdictreverse[add].upper())
            elif flag == 0:
                result.append(alphabetdictreverse[add])
        else:
            result.append(i)
    return result

def Szyfrowanie(mode):
    try:
        f=open("plain.txt", "r")
        plain = f.read()
        plain = normalize(plain)
        plain = list(plain)
        print(plain)
        f=open("key.txt", "r")
        key = f.read()
        print(key)
    except FileNotFoundError:
        print("Nie mozna znalezc potrzebnych plikow")
        return 0
    try:
        if mode == 1:
            for i in plain:
                flag = 0
                if i.isalpha():
                    if i.isupper():
                        flag = 1
                    add = (alphabetdict[i.lower()] + int(key))%26
                    if flag == 1:
                        result.append(alphabetdictreverse[add].upper())
                    elif flag == 0:
                        result.append(alphabetdictreverse[add])
                else:
                    result.append(i)
        elif mode == 2:
            key = key.split(" ")
            a = int(key[0])
            b = int(key[1])
            print(a,b)
            if nwd(a,26) != 1:
                print("klucz błędny")
                return 0
            for i in plain:
                flag = 0
                if i.isalpha():
                    if i.isupper():
                        flag = 1
                    add = ((alphabetdict[i.lower()] * a)+b)%26
                    if flag == 1:
                        result.append(alphabetdictreverse[add].upper())
                    elif flag == 0:
                        result.append(alphabetdictreverse[add])
                else:
                    result.append(i)
    except ValueError:
        print("Zly klucz")
        return 0
    except IndexError:
        print("Zly klucz")
        return 0
    result2 = "".join(result)
    f = open("crypto.txt", "w+")
    f.write(result2)





def Odszyfrowywanie(mode):
    try:
        f = open("crypto.txt", "r")
        crypto = f.read()
        crypto = list(crypto)
        print(crypto)
        f = open("key.txt", "r")
        key = f.read()
        print(key)
    except FileNotFoundError:
        print("Nie mozna znalezc potrzebnych plikow")
        return 0
    try:
        if mode == 1:
            result = decrypt(key,crypto)
        elif mode == 2:
            key = key.split(" ")
            a = int(key[0])
            b = int(key[1])
            x = 1
            if nwd(a,26) != 1:
                print("klucz błędny")
                return 0
            result = decryptaffi(crypto,a,b)
    except ValueError:
        print("Zly klucz")
        return 0
    except IndexError:
        print("Zly klucz")
        return 0
    result2 = "".join(result)
    f = open("decrypt.txt", "w+")
    f.write(result2)

def KryptozJawnym(mode):
    try:
        f=open("crypto.txt", "r")
        plain = f.read()
        plain = list(plain)
        print(plain)
        f=open("extra.txt", "r")
        key = f.read()
        klucz = list(key)[0]
        print(klucz)
    except FileNotFoundError:
        print("Nie mozna znalezc potrzebnych plikow")
        return 0
    if mode == 1:
        key = (alphabetdict[plain[0].lower()] - alphabetdict[klucz.lower()])%26
        result = decrypt(key,plain)
        wynik = "".join(result)
        f=open("decrypt.txt", "w+")
        f.write(wynik)
        f=open("key.txt", "w+")
        f.write(str(key))
    if mode == 2:
        if ekstratest(key) == 0:
            print("jawny nie pozwala na kryptoanalize")
            return 0
        CkeyA = key[0]
        CkeyB = key[1]
        keyA = plain[0]
        keyB = plain[1]
        print(keyA,keyB,CkeyA,CkeyB)

        zs1 = alphabetdict[keyA.lower()]
        zs2 = alphabetdict[keyB.lower()]
        zo1 = alphabetdict[CkeyA.lower()]
        zo2 = alphabetdict[CkeyB.lower()]
        # temp = (keyAint + 26 - keyBint)
        # ctemp = (CkeyAint + 26 - CkeyBint)
        resA = ((zs1 + 26 - zs2) * revmod(zo1 + 26 - zo2, 26)) % 26;
        resB = (zs2 + 26 - (resA * zo2) % 26) % 26;
        print(resA,resB)
        result = []
        x = 1
        if nwd(resA, 26) != 1:
            print("klucz błędny")
            return 0
        result = decryptaffi(plain,resA,resB)
        print(result)
        result2 = "".join(result)
        f = open("plain.txt", "w+")
        f.write(result2)
        f = open("key.txt", "w+")
        f.write(str(resA))
        f.write(" ")
        f.write(str(resB))

def kryptobezjawnego(mode):
    try:
        f=open("crypto.txt", "r")
        plain = f.read()
        plain = list(plain)
    except FileNotFoundError:
        print("Nie mozna znalezc potrzebnych plikow")
        return 0
    f= open("decrypt.txt","w+")
    result = []
    if mode == 1:
        for i in range(0,26):
            print(result)
            result.clear()
            result = decrypt(i,plain)
            result2 = "".join(result)
            f.write(result2)
            f.write("\n")
    elif mode == 2:
        for a in range(1,26):
            for b in range(1,12):
                if nwd(a,b) != 1:
                    continue
                print(a,b)
                result.clear()
                result = decryptaffi(plain,a,b)
                result2 = "".join(result)
                f.write(result2)
                f.write("\n")