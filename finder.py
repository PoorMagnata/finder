#!/usr/bin/env python

## FINDER VERSION 0.1 (ALPHA)
### FOR PROGRAMMERS: YES, I KNOW THAT MY CODE IS VERY UGLY AND BAD. I JUST MADE THIS FOR FUN, BUT I PRETEND TO IMPROVE IT ON THE FUTURE. YOU ARE WELCOME TO EDIT OR FORK.
### LICENSE: GNU GPL 3

import os, sys

paths = list(set(os.getenv("PATH").split(":")))
args = sys.argv

found = []

for i in range(len(paths)):
    try:
        found.extend(os.listdir(paths[i]))
    except FileNotFoundError:
        None

found = sorted(list(set(found)))
setExec = True
setGrid = False
setHelp = False
setKompakt = False
setArgs = 0

def searchGrid(num):
    spaces = "                                           "
    tokens = 0
    
    if num == 0:
        for i in range(len(found)):
            tokens = tokens+1
            if tokens < 4:
                print(f'{found[i]}{spaces[:-len(found[i])]}', end='',sep='')
            if tokens == 4:
                tokens = 0
                print(f'{found[i]}\n', end='', sep='')
    else:
        for i in range(len(found)):
            if args[num].lower() in found[i].lower():
                tokens = tokens+1
                if tokens < 4:
                   print(f'{found[i]}{spaces[:-len(found[i])]}', end='',sep='')
                if tokens == 4:
                    tokens = 0
                    print(f'{found[i]}\n', end='', sep='')
            
    print()
    
def searchList(num):
    if num == 0:
        if setGrid == False:
            for i in range(len(found)):
                print(found[i])
    else:      
        for i in range(len(found)):
            if args[num].lower() in found[i].lower():
                print(found[i])
                
def searchKompakt(num):
    if num == 0:
        if setGrid == False:
            for i in range(len(found)):
                print(f'{found[i]} ', end='' , sep='')
    else:      
        for i in range(len(found)):
            if args[num].lower() in found[i].lower():
                print(f'{found[i]} ', end='' , sep='')
    print()

if len(args) > 1:
    if "-h" in args[1] or "--help" in args[1]:
        setExec = False
        setArgs = True
        print("<==========> SHOWING: HELP SCREEN <==========>")
        print()
        print('''This program was 100% made on Python 3.12.4 by PoorMagnata (https://github.com/poormagnata/finder).
License: GNU GPL 3

About: This program was made for you to find your applications on Linux.

How does it works: The program will find all the files inside all the paths of your $PATH variable and will display on the screen for you. It can be a hundred times more faster and easier than typing "ls" on all your applications inside the paths on the $PATH variable, and using "grep" on those. This program is also exclude repeated files that are inside different locations on $PATH from the listing.

Use: finder <argument> <search>   OR   finder <search>
     (!) Only one word by search. Instead, you can use GREP: finder <argument> | grep "search"

Available arguments: No arguments (Displays the list in a list format); -h --help (Shows this screen); -g --grid (Displays the list in grid format); -k --kompakt (Displays the list in just one line).

Tip: If some program is missing from the list, just try to execute finder with superuser privileges (sudo finder).
''')
    elif "-g" in args[1] or "--grid" in args[1]:
        setGrid = True
        setArgs = True
    elif "-k" in args[1] or "--kompakt" in args[1]:
        setKompakt = True
        setArgs = True

if setExec == True:

    if setGrid == True:
        setExec = False
        if len(args) >= 3:
            searchGrid(2)
        else:
            if len(args) <= 2:
              searchGrid(0)
            else:
                searchGrid(0)
                
    
    if setKompakt == True:
        setExec = False
        if len(args) >= 3:
            searchKompakt(2)
        else:
            if len(args) <= 2:
              searchKompakt(0)
            else:
                searchKompakt(0)   
                
    if setExec == True:
        if setArgs == True:
           searchList(1)
        else:
            if len(args) <= 1:
                searchList(0)
            else:
                searchList(1)
