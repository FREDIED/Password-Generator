import random
import time
piska = '1234567890'
piskabobra ='qwertyuiopasdfghjklzxcvbnm'
pipiska = piskabobra.upper()
podpiska = piska+piskabobra+pipiska
x = (int(input("    Какая длинна? \n    ")))
clozhna = input("   Использовать русский алфавит?\n")
if clozhna == "n":
    clozhna2 = input("    Использовать всякую бяку?\n")
    if clozhna2 == "n":
        piska = '1234567890'
        piskabobra ='qwertyuiopasdfghjklzxcvbnm'
        pipiska = piskabobra.upper()
        podpiska = piska+piskabobra+pipiska
        ls = list(podpiska)
        random.shuffle(ls)
        psw = ''.join([random.choice(ls) for x in range(x)])
        print(psw)
        time.sleep(10)
    if clozna2 == "y":
        pipirkabobra = "!@#$%^&*()_+-=?><:""}{\\|}相機相機電視電視電視快餐帳篷回起來"
        piska = '1234567890'
        piskabobra ='qwertyuiopasdfghjklzxcvbnm'
        pipiska = piskabobra.upper()
        podpiska = piska+piskabobra+pipiska+pipirkabobra
        ls = list(podpiska)
        random.shuffle(ls)
        psw = ''.join([random.choice(ls) for x in range(x)])
        print(psw)
        time.sleep(10)
if clozhna == "y":
    pipirka = "йцукенгшщзхъёфывапролджэячсмитьбю"
    clozhna2 = input("    Использовать всякую бяку?\n")
    if clozhna == "n":
        piska = '1234567890'
        piskabobra ='qwertyuiopasdfghjklzxcvbnm'
        pipiska = piskabobra.upper()
        podpiska = piska+piskabobra+pipiska+pipirka
        ls = list(podpiska)
        random.shuffle(ls)
        psw = ''.join([random.choice(ls) for x in range(x)])
        print(psw)
        time.sleep(10)
    if clozhna2 == "y":
        pipirkabobra = "!@#$%^&*()_+-=?><:""}{\\|}"
        piska = '1234567890'
        piskabobra ='qwertyuiopasdfghjklzxcvbnm'
        pipiska = piskabobra.upper()
        pipipiska = pipirka.upper()
        podpiska = piska+piskabobra+pipiska+pipipiska+pipirkabobra
        ls = list(podpiska)
        random.shuffle(ls)
        psw = ''.join([random.choice(ls) for x in range(x)])
        print(psw)
        time.sleep(10)
