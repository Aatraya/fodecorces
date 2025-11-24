import os
import time
import sys
from Problems import Problem
from judge1 import Judge 
from submissions import submissions, create_submission_directory 

i=0

#making base directory where my submission go into
base_dir = "submission_data"
os.makedirs(base_dir, exist_ok=True) #making sure it exists

# intialising the judging system

judge_sys = Judge()

def createProblem():
    prbid = input("Enter problem id: ")
    titl = input("Enter problem title: ")
    des = input("Enter description for problem: ")
    cons = input("Enter constraints: ")
    tests = eval(input("Enter the test cases as list of tuples where each element is a string: "))
    tl = int(input("Enter time limit (in seconds): "))
    ml = int(input("Enter Memory limit (in MB): "))


def createProblemW():
    # Write problem description and testcases to files
    prb.write_problem()
    prb.write_testcase()
    print(f"Problem {prbid} created.")



def doSubmit():
    subid = i #clarify once
    uid = input("Enter user id: ")
    pid = input("Enter the problem id: ")
    try:
        prb = problems[pid]
    except KeyError:
        print("FodeCorces doesn't host this problem.")
        return
    
    lang = input("Enter language: (python/java/c/cpp)")
    if prb is None:
        print("Problem dont exist bruh")
        return


    def get_code_from_terminal():
        print("Paste your code below (press Ctrl+D or Ctrl+Z then Enter to finish):")
        # Reads all lines until EOF (Ctrl+D on Linux/macOS, Ctrl+Z on Windows)
        code_input = sys.stdin.read()
        return code_input

    subcode = get_code_from_terminal()
    timestamp = time.time()

    sub = submissions(
        subid,
        uid,
        pid,lang,
        subcode,
        timestamp
        )

    code_path = sub.get_code(base_dir)
    sub.metadata()
    print(f"Submission {subid} saved to: {code_path}")
    testcases_judge = prb.judge_test_cases()
    print("\nStarting judge ")
    result = judge_sys.judge(code_path, lang, testcases_judge)

    print("Judge result:")
    print(f"Overall Status: **{result['overall']}**")


    for detail in result['details']: #displaying the results 
        print(f"Input: '{detail['input']}' | Status: {detail['status']}")
        if detail['status'] == 'FAIL':
            print(f"  Got: {detail['got']} | Expected: {detail['expected']}") # showing comparison of test cases

problems={}
while True:
    print("Menu options:")
    print("1. Create a problem: ")
    print("2. Submit a problem: ")
    print("3. Exit")
    choice = int(input("Enter choice:"))
    if(choice==1):
        prbid = input("Enter problem id: ")
        titl = input("Enter problem title: ")
        des = input("Enter description for problem: ")
        cons = input("Enter constraints: ")
        tests = eval(input("Enter the test cases as list of tuples where each element is a string: "))
        tl = int(input("Enter time limit (in seconds): "))
        ml = int(input("Enter Memory limit (in MB): "))
        prb = Problem(
                    prbid, 
                    titl, 
                    des, 
                    cons, 
                    tests, 
                    tl, 
                    ml
                )
        problems[prbid]=prb

        createProblemW()
    elif(choice==2):
        doSubmit()
        i+=1
    elif(choice==3):
        print("Thanks for believing in the idea of FodeCorces. We hope you solve again soon.")
        break
    else:print("You did not enter a correct choice, please read again as ICPC does not encourage mistakes.")









    
