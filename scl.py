import time
import random
import math
import sclf
import pickle

print("welcome to Simple Coding Language.")
print("")
while True:
    print("")
    print("1>>>[file]")
    print("2>>>[console]")
    inp = input(">>>")
    #the file
    if inp == "1":
        print("do you want to delete the old project?")
        inp = input(">>>")
        #look at if there was any old saved data
        if inp == "no":
            with open('save.py', 'rb') as fp:
                alinp = pickle.load(fp)
                a = True
                for count in range(len(alinp)):
                    print(count,">>",alinp[count])
                while a == True:
                    inp = input(print(len(alinp),">> "))
                    inpsp = inp.split(" ")
                    if inp == "run":
                        print(">>> running program_")
                        print("")
                        time.sleep(2)
                        sclf.runscl(alinp)
                    elif inp == "exit":
                        a = False
                    elif inp == "save":
                        with open('save.py', 'wb') as fp:
                            pickle.dump(alinp, fp)
                    elif inpsp[0] == "edit":
                        for count in range(len(alinp)):
                            count = str(count)
                            if inpsp[1] == count:
                                inp = input(print(count,">>>"))
                                alinp[int(count)] = inp
                    else:
                        alinp = alinp + [inp]
        if inp == "yes":
            alinp = []
        if alinp == []:
            a = True
            #line count for display
            lc = 0
            while a == True:
                #increase the line count by 1
                lc = lc + 1
                inp = input(print(len(alinp),">>"))
                inpsp = inp.split(" ")
                if inp == "run":
                    print(">>> running program_")
                    print("")
                    time.sleep(2)
                    sclf.runscl(alinp)
                elif inp == "exit":
                    a = False
                elif inp == "save":
                    with open('save.py', 'wb') as fp:
                        pickle.dump(alinp, fp)
                elif inpsp[0] == "edit":
                    for count in range(len(alinp)):
                        count = str(count)
                        if inpsp[1] == count:
                            inp = input(print(count,">>>"))
                            alinp[int(count)] = inp
                else:
                    alinp = alinp + [inp]
    if inp == "2":
        print("scl console:")
        a = True
        while a == True:
            inp = input(">>>")
            if inp == "exit":
                a = False
            else:
                sclf.runscl([inp])
    if inp == "3":
        quit()
