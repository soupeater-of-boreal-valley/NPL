import random
import time
import math

def runscl(alinp):
    classes = []
    clspk = []
    v = []
    clas = ""
    a = ""
    mat = 0
    ran = 0
    tb = 0
    for count in range(len(alinp)):
        inp = alinp[count]
        inpsp = inp.split(" ")
        if inpsp[0] == "send{":
            inpsp[0] = ""
            for count in range(len(inpsp) - 1):
                if inpsp[count] == "v":
                    inpsp[count] = v[int(inpsp[count + 1])]
                    inpsp[count + 1] = ""
                if inpsp[count] == "inp":
                    inpsp[count] = a
                inpsp[0] = inpsp[0] + " " + inpsp[count + 1]
            print(inpsp[0])
        if inpsp[0] == "inp{}":
            a = input()
        if inpsp[0] == "crtv{":
            if inpsp[1] == "inp":
                v = v + [a]
            else:
                v = v + [inpsp[1]]
        if inpsp[0] == "ifinp{":
            if inpsp[1] == "=":
                if inpsp[2] == "v":
                    if a != v[int(inpsp[3])]:
                        alinp[count + 1] = ""
                elif a != inpsp[2]:
                    alinp[count + 1] = ""
                else:
                    asdf = 1
            if inpsp[1] == "!":
                if inpsp[2] == "v":
                    if a == v[int(inpsp[3])]:
                        alinp[count + 1] = ""
                elif a == inpsp[2]:
                    alinp[count + 1] = ""
                else:
                    asdf = 1
        if inpsp[0] == "while{":
            if inpsp[1] == "v":
                w1 = v[int(inpsp[2])]
            elif inpsp[1] == "inp":
                w1 = a
                inpsp = inpsp + [""]
                inpsp[4] = inpsp[3]
                inpsp[3] = inpsp[2]
            else:
                return print("error: nothing assigned to compare for while.1")
            if inpsp[3] == "inp":
                w2 = a
            elif inpsp[3] == "v":
                w2 = v[int(inpsp[4])]
            else:
                return print("error: nothing assigned to compare for while.2")
            alip = []
            w3 = 0
            sd = 0
            for count1 in range(len(alinp) - count):
                if alinp[count1 + count] == "break{}":
                    w3 = count1
                else:
                    s = alinp[count1 + count].split(" ")
                    if s[0] == "while{":
                        sd = 1
                    if w3 == 0:
                        if sd == 1:
                            alip = alip + [alinp[count1 + count + 1]]
            w3 = 0
            if w1 != w2:
                for count2 in range(count1+1):
                    alinp[count + count2 - 1] = ""
            else:
                while w1 == w2:
                    for count2 in range(count1):
                        runscl(alip)
        if inpsp[0] == "end{}":
            return print("000end000")
        if inpsp[0] == "editv{":
            if inpsp[1] == "v":
                v[int(inpsp[2])] = inpsp[3]
        if inpsp[0] == "ifv{":
            inpsp[1] = v[int(inpsp[1])]
            if inpsp[2] == "v":
                inpsp[2] = v[int(inpsp[3])]
            if inpsp[1] == inpsp[2]:
                asdf = ""
            else:
                alinp[count + 1] = ""
        if inpsp[0] == "wait{":
            if inpsp[1] == "v":
                inpsp[1] = v[int(inpsp[2])]
            if inpsp[1] == "inp":
                inpsp = a
            time.sleep(int(inpsp[1]))
        if inpsp[0] == "import{":
            if inpsp[1] == "math":
                mat = 1
            if inpsp[1] == "random":
                ran = 1
            if inpsp[1] == "textbased":
                tb = 1
        if tb == 1:
            if inpsp[0] == "ifclas{":
                if inpsp[1] == "v":
                    inpsp[1] = v[int(inpsp[2])]
                if inpsp[1] == "inp":
                    inpsp[1] = a
                if clas == inpsp[1]:
                    asdf = ""
                else:
                    alinp[count + 1] = ""
            if inpsp[0] == "crten{":
                en = []
                enhp = []
                endam = []
                en = en + [inpsp[1]]
                enhp = enhp + [int(inpsp[2])]
                endam = endam + [enhp[len(enhp) - 1] / 1.5]
            if inpsp[0] == "clsp{}":
                for count1 in range(len(clspk)):
                    if a == clspk[count]:
                        clas = clspk[count]
            if inpsp[0] == "crtclas{":
                if len(inpsp) >= 5:
                    return print("error in code line:", alinp[count], ",'crtclass{' command overflow.")
                else:
                    print(inpsp[3], "| class:", inpsp[1])
                    print("hp:", inpsp[2])
                    classes = classes + [inpsp[1]]
                    clspk = clspk + [inpsp[3]]
        if ran == 1:
            if inpsp[0] == "d{":
                v = v + [ 1 + math.floor(int(inpsp[1]) * random.random()) ]
            if inpsp[0] == "vpick{}":
                v = v + [random.choice(v)]
            if inpsp[0] == "random{}":
                v = v + [random.random()]
        if mat == 1:
            vt = False
            if inpsp[0] == "add{":
                if inpsp[1] == "inp":
                    inpsp[1] = a
                if inpsp[1] == "v":
                    vt = True
                    inpsp[1] = v[int(inpsp[2])]
                else:
                    asdf = 1
                if vt == False:
                    if inpsp[2] == "inp":
                        inpsp[2] = a
                    elif inpsp[2] == "v":
                        inpsp[2] = v[int(inpsp[3])]
                    else:
                        asdf = 1
                else:
                    if inpsp[3] == "inp":
                        inpsp[2] = a
                    if inpsp[3] == "v":
                        inpsp[2] = v[int(inpsp[4])]
                    else:
                        asdf = 1
                v = v + [int(inpsp[1]) + int(inpsp[2])]
            if inpsp == "x{":
                if inpsp[1] == "inp":
                    inpsp[1] = a
                if inpsp[1] == "v":
                    vt = True
                    inpsp[1] = v[int(inpsp[2])]
                else:
                    asdf = 1
                if vt == False:
                    if inpsp[2] == "inp":
                        inpsp[2] = a
                    elif inpsp[2] == "v":
                        inpsp[2] = v[int(inpsp[3])]
                    else:
                        asdf = 1
                else:
                    if inpsp[3] == "inp":
                        inpsp[2] = a
                    if inpsp[3] == "v":
                        inpsp[2] = v[int(inpsp[4])]
                    else:
                        asdf = 1
                v = v + [int(inpsp[1]) * int(inpsp[2])]
                
