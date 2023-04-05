import pickle
import sclf as sc

with open('save.py', 'rb') as fp:
    alinp = pickle.load(fp)

while True:
    print("running with : scl_runner")
    print("support the creator by giving me more money.")
    print("_____________________________________________________________________________________________________________")
    sc.runscl(alinp)
    print("_____________________________________________________________________________________________________________")
    print("end of game.")
    print("run again?")
    a2 = input("Y/N:")
    if a2 != "N":
        asd = 1
    else:
        quit()
