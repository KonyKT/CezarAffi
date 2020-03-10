import argparse
import sys
from operations import *



argumenty = ['-c','-a','-e','-d','j','k']
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c', action='store_true', help='szyfr Cezara')
group.add_argument('-a',  action='store_true',  help='szyfr afiniczny')
group2 = parser.add_mutually_exclusive_group(required=True)
group2.add_argument('-e', action='store_true',  help='szyfrowanie')
group2.add_argument('-d',  action='store_true',  help='odszyfrowywanie')
group2.add_argument('-j', action='store_true',  help='kryptoanaliza z tekstem jawnym')
group2.add_argument('-k',  action='store_true',  help='kryptoanaliza w oparciu o kryptogram')




def checkArgs():
    if len(sys.argv) != 3:
        print("zla liczba argumentów")
        return 0







def Cezar():
    if '-e' in sys.argv:
        Szyfrowanie(1)
    elif '-d' in sys.argv:
        Odszyfrowywanie(1)
    elif '-j' in sys.argv:
        KryptozJawnym(1)
    elif '-k' in sys.argv:
        kryptobezjawnego(1)

def Afiniczny():
    if '-e' in sys.argv:
        Szyfrowanie(2)
    elif '-d' in sys.argv:
        Odszyfrowywanie(2)
    elif '-j' in sys.argv:
        KryptozJawnym(2)
    elif '-k' in sys.argv:
        kryptobezjawnego(2)

if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])
    checkArgs()
    if '-c' in sys.argv:
        Cezar()
    elif '-a' in sys.argv:
        Afiniczny()
