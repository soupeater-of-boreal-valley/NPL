                                        ***SIMPLE CODEING LANGAUGE***
Hi, this is a simple codeing langauge i made for fun. It is made with python so don't expect it to run fast.

if you find a bug or are having issue with programming useing scl i am happy to help you.

                                                ***scl.py***
scl.py is the file that i made to let me actualy use the langauge to program.
scl.py needs save.py and sclf.py to function.

here are the commands:
                                                COMMAND LISTS
_____________________________________________________________________________________________________________                         
command list for main:

* save
--- saves the program.

* run
--- runs the program.

* exit
--- sends you back to the starting menu.

* import{ lib.
--- gives you access to more functions

* send{ txt
--- writes whatever is place were *txt* is.

* inp{}
--- lets the player enter an input that is used by other commands.

* crtv{ meaning
--- makes a variable that can be changed or used in other commands.

* ifinp{ = obj.
--- compares the previous input to whatever is placed in the *obj.*.

* while{ obj. obj.
--- repeats the same command until the two *obj.* are diffrent.

* break{}
--- makes the "while" command not repeat whatever is writen after it.

* end{}
--- ends the program.

* editv{ v num. meaning
--- changes the meaning of a variable

* ifv{ num. obj. (if obj = v)num.
--- compares a variable to whatever is placed in the *obj.*.

* wait{ secs.
--- makes the program stop for a number of seconds.

                                  ____________________________________________
command list for random:

* d{ num.
--- creates a variable that is 1-*num.*.

* vpick{}
--- creates a variable this is = a random variable that has perviously been created.

* random{}
--- creates a veriable that is 0-1 (decimals).

                                  ____________________________________________
command list for textbased:

* crtclas{ name hp picknum.
--- gives enother option for the player to pick in "clsp{}" and sets hp for the class.

* clsp{}
---lets player pick a class made by "crtclas{" when player inputs the number of *picknum.*.

* crten{ enname enhp
n- enemy damage is set to enemy hp / 1.5.
--- creates an enemy.

* ifclas{ obj (if obj. = v)num.
--- compares the picked class to whatever is placed in the *obj.*.

                                  ____________________________________________
* will be added later *
command list for math:

* add{ obj. obj.
--- adds the two obj together (if it is a variable write v num.)

* x{ obj. obj.
--- same as add{ but multiply instead of add

                                  ____________________________________________
                                 
                                 

                                       ---tutorial for scl.py interface---
start screen:
---
welcome to Simple Coding Language.


1>>>[file]
2>>>[console]
>>>_
---
from here write: 1
it should look like this:
---
welcome to Simple Coding Language.


1>>>[file]
2>>>[console]
>>>1
do you want to delete the old project?
>>>_
---
then you can say yes or no, if you say yes it will delete whatever is saved on save.py
i have a very simple example program saved on save.py
---
do you want to delete the old project?
>>>no
0 >> crtv{ 1
1 >> send{ robot: hello, i am robot.
2 >> while{ v 0 v 0
3 >> inp{}
4 >> ifinp{ = hi
5 >> send{ robot: hi, what is your favorate colour?
6 >> ifinp{ = blue
7 >> send{ robot: that is interesting.
8 >> ifinp{ = blue
9 >> wait{ 3
10 >> ifinp{ = blue
11 >> end{}
12 >> ifinp{ = yellow
13 >> send{ robot: i don't like yellow.
14 >> ifinp{ = yellow
15 >> end{}
16 >> ifinp{ robot: good choice. what do you think about the stars in the sky?
17 >> inp{}
18 >> end{}
19 >> break{}
20 >>
None_
---
if you chose to delete the old file
---
do you want to delete the old project?
>>>yes
0 >>
None
---
it shows you a blank file.

*note - it says None before were you type, that is a bug, i am trying to fix it so wish me luck but for now it changes nothing exept of visual and you can view all
        of what you wrote normaly if you just save and exit.

                                                      WHY?
a question i commonly ask myself is why did i do this? well by making this i have learned a lot and can now also add more to the
langauge and slowly make it better then python. it is also given me things to do over the holiday.

                                            WHAT I PLAN TO DO WITH IT.
i plan to update the interface to make it easier to navigate and i plan to make the saveing system better. it is possable that
i will make a complate redisgn and change the name of the file in the future.

                                               ***scl runner.py***

scl runner.py needs sclf.py and save.py to function. it is simply a file that runs the program saved on save.py without needing to go through the code.

                                            WHAT I PLAN TO DO WITH IT.
i don't see much of a reason to update the runner since it will run at the same update as your sclf.py file so there is not much
in the future off scl runner exept of possably changing it so you can pick what file you will run with it at the start of each cycle and what is says at the start.

                                                  ***sclf.py***
sclf.py is the part wich holds the code that changes a python list into the output that runs in scl.py and scl runner.py it does not need anything but
python to work and can be used as an import to change whatever you put into "sclf.runscl(alinp)" into scl code.

                                            WHAT I PLAN TO DO WITH IT.
there will be meany upgrades to sclf.py, it is currantly at 1.05.

                                              ---PREVIOUS UPDATES---
---1.06
NEW FEATURES:
* math import
* add{ command
* x{ command

---1.05
NEW FEATURES:
* imports
* added the random import
* moved textbased rpg commands into desegnated import
* crten{ command
* a readme file

BUG FIXES:
* fixed "editv{" bug.

---1.04
NEW FEATURES:
* wait{ command
* ifv{ command

BUG FIXES:
* fixed variables

---1.03
 - NO NEW FEATURES -

BUG FIXES:
* fixed some of the while command
* fixed saves

---1.02

NEW FEATURES:
* while command
* saves

 - NO BUG FIXES -

---1.01

NEW FEATURES:
* all og commands.

 - NO BUG FIXES -



                                              ---FUTURE UPDATES---
FEATURES:
* graphs
* def{ command
* scl.py interface update
* potential scl runner update
* get a logo

BUG FIXES:
* crtv{ with multiple words
* while{ inp fix
* send{ inp fix
* send{ v x fix
* general if command fix
* fix the None bug
