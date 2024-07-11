# About
This program was 100% made on Python 3.12.4 by PoorMagnata (https://github.com/poormagnata/finder).
License: GNU GPL 3

About: This program was made for you to find your applications on Linux.

How does it works: The program will find all the files inside all the paths of your $PATH variable and will display on the screen for you. It can be a hundred times more faster and easier than typing "ls" on all your applications inside the paths on the $PATH variable, and using "grep" on those. This program is also exclude repeated files that are inside different locations on $PATH from the listing.

Use: finder <argument> <search>   OR   finder <search>
     (!) Only one word by search. Instead, you can use GREP: finder <argument> | grep "search"

Available arguments: No arguments (Displays the list in a list format); -h --help (Shows this screen); -g --grid (Displays the list in grid format); -k --kompakt (Displays the list in just one line).

Tip: If some program is missing from the list, just try to execute finder with superuser privileges (sudo finder).

# Installing
Copy and paste this on your terminal:
```
echo "'finder' is installing...\n\n\n"&&cd ~/Downloads/&&sudo rm -rf PoorMagnataFinder&&git clone https://github.com/PoorMagnata/finder PoorMagnataFinder&&cd PoorMagnataFinder&&sudo chmod +x finder.py&&if [ -f /usr/bin/finder ];then echo "\n\n\n'finder' will not be installed because there is already a program called 'finder' inside your /usr/bin/finder. Use 'rm -rf /usr/bin/finder' to fix it if you know what you are doing.\n\n\nFinished with an error, 'finder' was not installed.";else sudo mv -vn finder.py /usr/bin/finder && echo "\n\n\n'finder' was sucessfully installed.";fi;
```

# Uninstalling
Copy and paste this on your terminal:
```
echo "'finder' is being uninstalled...\n\n\n"&&sudo rm -rf /usr/bin/finder&&sudo rm -rf ~/Downloads/PoorMagnataFinder&&echo "\n\n\n'finder' sucessfully uninstalled from your system."
```
