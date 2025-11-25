# FODECORCES README FILE

This project is made by team Fodecorces . This team has the following members:

- Aatraya Mukherjee(IC2025004)
- Kedar Mallya(BC2025043)
- Nevaan Jain(BC2025068)

This project allows you to enter a problem and its testcases and submit solutions to such problems . It then evaluates and compiles them to give output . 


## CONCEPTS USED

* Classes 
* Function 
* File I/O
* Menu Driven Programming
* Terminal Command executed by program
* User build libraries

## LIBRARIES USED
* os
* time
* sys
* subprocess
* ast


## DEPENDENCIES TO RUN THE CODE 
* All the above packages need to be installed
* gcc and g++ compilers should be installed

## HOW IT WORKS

### STEP BY STEP EXPLAINATION OF IMPORTS IN MAIN.PY:

* from Problems import Problem: 
a class Problem is made in Problems, which has functions to add a question, its limits, and testcases for the question. this problem is then saved in a text file in the same directory as program

* from judge1 import Judge: 
responsible to execute the given code submitted by user. the code entered by user is run on another terminal. uses cmd to enter commands in new terminal, encode() to fit in inputs, try & expect to check if the code enter may have compilation errors. gives status of the code on each testcase as well

* from submissions import submissions, create_submission_directory: 
submissions is a class. it writes the code entered by the user into a file of corresponding language so it is ready to be executed, makes a metadata.txt file to store all data: from code to limits to directory. everything is stored in this file to store as history. it can also connect base directory to problem and submission files

### BRIEF EXPLAINATION OF STEPS CARRIED IN MAIN.PY:

* load_existing_function():
every file in the directory is checked. if there exists a file ending with 'Description', it is recognised as a problem's description and gets the testcases with it. the file is read and the title, description and limits are taken from it. then it is converted into an object

* createproblemW():
takes the user inputs and makes it into a document with the help of Problem class functions

* doSubmit():
this function takes the code submission from user and connects main.py to Judge class and submissions class, runs it and gives user the status of his code or how his code performed for the problem

* after the functions made, memory for problems is made and the pre existing problems are stored. then code for the menu interactions is made. this code is rigorous to make sure the flow of code is maintained. 

## EXAMPLE I/O



## ROLES

- Aatrata Mukherjee: problem.py, main.py
- Kedar Mallya: submissions.py, judge.py
- Nevaan Jain: main.py, readme.md

## LIMITATIONS OF OUR CODE

* supports only 3 languages: c, c++ and python
* does not check for memory limit exceeded
* uses txt file instead of csv
